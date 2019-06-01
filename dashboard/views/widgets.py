from datetime import date

from django.utils import timezone
from django.db.models import Sum
from django.utils import timezone
from django.db.models import Q, Sum

# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from shared.views import TimeDelayed_APIView
from dashboard.models import Users, UserProfile, Widget, Roles


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

        return ''

        
    def profilewidget(self, request):
        user = request.user
        profile = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'personal_mobile_no': '',
            'dob': '',
            'media': ''
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
        qs_json = ''
        return Response(qs_json)


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