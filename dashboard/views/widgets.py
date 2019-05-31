from datetime import date

from django.utils import timezone
from django.db.models import Sum
from django.utils import timezone
from django.db.models import Q, Sum

# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shared.views import TimeDelayed_APIView
from events.models import Event
from students.models import Student
from dashboard.models import Users, UserProfile, Widget, Roles
from hr.models import Holiday
from students.models import StudentSerializer
from fees.serializers import FeeCategoryDetailsSerializer
from fees.views import FeeHelper
from academics.models import Assignment, AssignClasswiseTeacher, AcademicYear
from timetable.models import TimeTable
from reports.views.students import TermWiseReportViewSet
from academics.models import StudentsAttendence, ClassWorkingDays

# from dashboard.tasks.student_averagemarks import student_average_task


class getuserWidgets(TimeDelayed_APIView):
    """
    To get Widgets of the loggedin User --> http://localhost:4200/home/dashboard/
    """
    # permission_classes = (IsAuthenticated,)
    def get_user_academic_class(self, request):
        """
        input: request.user, output: academic_class
        """
        user = request.user
        
        # if request.user -> teacher, student, parent
        if hasattr(user, 'student'):
            # student
            return user.student.myclass
        
        if hasattr(user, 'parents'):            
            # if parents parent then show first student's timetable
            activestudent = self.get_activestudent(request)
            return activestudent.student.myclass

        if AssignClasswiseTeacher.objects.filter(teacher = user):
            # teacher
            return AssignClasswiseTeacher.objects.get(teacher = user,deleted_at=None,status=1).available_class
        return ''

    def guagegraph(self, user):
        # student_average_task()
        termwise = TermWiseReportViewSet()
        (t_graph, m_entries, academicyear) = termwise.get_graphdata(user,user)

        items = [m[1] for m in t_graph]
        average = sum(items)/len(items) if items else 0
        return round(average, 0)

    def getyearlyattendance(self,user):
        absents = StudentsAttendence.objects.filter(
            attendence__academic_year__status= 1, deleted_at = None
        ).count()
        workingdays = ClassWorkingDays.objects.filter(
            academic_year__status = 1, 
            assign_class=user.student.myclass.class_name
            ).aggregate(Sum('no_of_days'))['no_of_days__sum']
        if not workingdays:
            percentage = 0
        else:
            percentage = ((workingdays-absents)/workingdays) * 100

        return percentage
        
    def profilewidget(self, request):
        user = request.user
        student = ''
        if hasattr(user, 'student'):
            serializer = StudentSerializer(user.student, context={'request': request})
            student = serializer.data
        
        profile = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'personal_mobile_no': '',
            'dob': '',
            'media': '',
            'student': student
        }
        if hasattr(request.user, 'userprofile'):
            profile['personal_mobile_no']= user.userprofile.personal_mobile_no,
            profile['dob']= user.userprofile.dob,
            profile['media']= request.build_absolute_uri(user.userprofile.media.url) if user.userprofile.media else '',
        
        return profile

    def get_activestudent(self, request):

        # activechild = request.GET['activechild']
        # if activechild == 'first':
        #     return request.user.parents.student.all()[0]
        # return Users.objects.get(id = request.GET['activechild'])
        return request.user.parents.active_student

    def get(self, request, format=None):
        resp = {'widgets': ''}  # []
        if hasattr(request.user, 'userroles'):
            cur_month = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0) # timezone.localdate().replace(day=1)  
            widgets = request.user.userroles.role.widgets.all()
            resp['widgets'] = [w.code for w in widgets]

            if 'profile' in resp['widgets']:
                resp['profile'] = self.profilewidget(request)

            if 'fees' in resp['widgets']:
                resp['fees'] = []
                if hasattr(request.user, 'student'):
                    feehelper = FeeHelper(request.user.student)

                    serializer = FeeCategoryDetailsSerializer(feehelper.get_unpaid_fees(), many=True)
                    resp['fees'] = serializer.data

            if 'events' in resp['widgets']:
                resp['events'] = Event.objects.filter(start_date__gte=cur_month).values()

            if 'noticeboard' in resp['widgets']:
                resp['noticeboard'] = []

            if 'holidays' in resp['widgets']:
                resp['holidays'] = Holiday.objects.filter(start_date__gte=cur_month).values()

            if 'assignment' in resp['widgets']:
                resp['assignment'] = []

            if 'timetable' in resp['widgets']:                
                resp['timetable'] = '' # if empty will display there is no time table
                a_class = self.get_user_academic_class(request)                    
                if a_class:
                    a_year = AcademicYear.objects.get(status = 1)
                    timetable = TimeTable.objects.filter(academic_year=a_year, academic_class=a_class)
                    if timetable:
                        resp['timetable'] = timetable[0].id

            
            if any(hasattr(request.user, attr) for attr in ['student', 'parents']):
                # if hasattr(request.user, 'student') or hasattr(request.user, 'parent'):                
                if hasattr(request.user, 'parents'):
                    graph_user = self.get_activestudent(request)
                    # request.user.parents.student.all()[0]
                else:
                    graph_user = request.user

                resp['guagegraph'] = self.guagegraph(graph_user)
               
                # ['Extracurricular', 'Exam', 'Attendance', 'Psychometric', 'Other']
                resp['spiderwebgraph'] = [
                    43.0,  # Extracurricular
                    resp['guagegraph'],  # Exam
                    self.getyearlyattendance(graph_user), # Attendance
                    30, # Psychometric
                    17 # Other
                ]
            
        return Response(resp)


class getFullCalenderEvents(TimeDelayed_APIView):
    """
    To show events in calendar --> http://localhost:4200/home/calendar/
    """
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        events = Event.objects.all()
        qs_json = [dict(id=et.id, title=et.event_name, event_name=et.event_name,
                        event_type=et.event_type.type_name,
                        color=et.event_type.color_code,
                        event_location=str(et.event_location),
                        event_desc=str(et.event_desc), start=str(et.start_date), end=str(et.end_date),
                        start_date=str(et.start_date), end_date=str(et.end_date)) for et in events]
        
        # show fee due in calendar
        if hasattr(request.user, 'student'):
            feehelper = FeeHelper(request.user.student)
            for feecategorydetails in feehelper.get_unpaid_fees():
                qs_json.append({"color": "#ccc", 
                    'title': "{0} - {1}Rs.".format(feecategorydetails.category.name,feecategorydetails.amount), 
                    'start': str(feecategorydetails.category.due_date)})
                
        return Response(qs_json)  # JsonResponse(qs_json,safe=False)


class getUserBirthdays(TimeDelayed_APIView):
    """
    To show birthdays onthe right side of calendar --> http://localhost:4200/home/calendar/
    """
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        today = timezone.now() # timezone.localtime(timezone.now())
        print(today.month,today.day)
        user_profiles = UserProfile.objects.filter(status=1, deleted_at=None, dob__month=today.month,
                                                   dob__day=today.day)
        qs_json = []
        for st in user_profiles:
            if st.user.user_type == 'S':
                qs_json.append(dict(id=st.id, student_name=st.user.first_name+' '+st.user.last_name, class_name=st.user.student.myclass.class_name,
                        divison=st.user.student.myclass.class_division))
        return Response(qs_json)  # JsonResponse(qs_json,safe=False)

class getRoleWidgets(TimeDelayed_APIView):
    """
    To fill Widgets multiselect box in --> http://localhost:4200/dashboard/widgetpermission
    """

    def get(self, request, format=None):
        roleid = request.GET['roleid']
        role = Roles.objects.get(id = roleid)
        x = role.role_type
        # https://stackoverflow.com/a/4184425/2351696
        widgets = Widget.objects.filter( 
            Q(roletypes__startswith=x+',') | 
            Q(roletypes__endswith=','+x) | 
            Q(roletypes__contains=',{0},'.format(x)) | 
            Q(roletypes__exact=x) |
            Q(roletypes='') 
        )
        return Response(widgets.values('id','name','code'))