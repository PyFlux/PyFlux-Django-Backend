from dashboard.models import Users, UserProfile
from rest_framework.views import APIView
from parents.models import Parents
from parents.serializers import ParentSerializer
from students.models import Student, StudentMaster
from academics.models.Classes import Classes
from academics.models.Assignment import Assignment
from django.db.models import Q
from dashboard.models import *
from shared.views import TimeDelayed_APIView
from academics.models import Assignment,AssignClasswiseTeacher,StudentAssignment
from academics.serializers import AssignmentSerializer,AssignClasswiseTeacherSerializer,StudentAssignmentSerializer
from rest_framework.response import Response
from dashboard.serializers import UserProfilesSerializer, UsersSerializer


class getAssignment(TimeDelayed_APIView):
   
    def get(self, request, format=None):
       
        data = request.data
        
        userid  = request.user.id
        usertype  =  Users.objects.filter(id = userid,deleted_at=None)
        if usertype[0].user_type == 'S':
            

            student_details = Student.objects.filter(user_id = userid,deleted_at=None)
            classid = student_details[0].myclass_id
           

            assignment_class = Assignment.objects.filter(Q(class_division=classid) & Q(deleted_at=None) & ~Q(status = 0) & ~Q(status = 3 ))
            classes = Classes.objects.filter(id =classid)
            classname = classes[0].classname
           
            queryset = StudentAssignment.objects.filter(student = userid, deleted_at=None)
            
            result = []
            for query in queryset:
                
                
                queryset2 = Assignment.objects.filter(id = query.assignment_id, deleted_at=None)
                for query2 in queryset2:
                    
                    queryset3 =  dict(id = query2.id,
                    name = query2.name,
                    description = query2.description,
                    start_date = query2.start_date,
                    end_date = query2.end_date,
                    marks = query2.marks,
                    )

                

                    queryset3.update({'classname':classname,'student_id':userid,'status': query.status})

                    result.append(queryset3)

            return Response(result)
       

        elif usertype[0].user_type == 'P':
            
            parent = Parents.objects.get(user_id = userid,deleted_at=None)

            
            for student in parent.student.all():
                queryset = Student.objects.filter(user_id = student.id,deleted_at=None)
                classid = queryset[0].myclass_id

                assignment_class = Assignment.objects.filter(Q(class_division=classid) & Q(deleted_at=None) & ~Q(status = 0 ) & ~Q(status = 3 ))
                if(assignment_class):
                    classes = Classes.objects.filter(id = classid)
                    classname = classes[0].classname
                    queryset = StudentAssignment.objects.filter(student = student.id, deleted_at=None)
                    

                    result = []
                    for query in queryset:
                        queryset2 = Assignment.objects.filter(id = query.assignment_id, deleted_at=None)
                        for query2 in queryset2:
                            queryset3 =  dict(id = query2.id,
                            name = query2.name,
                            description = query2.description,
                            start_date = query2.start_date,
                            end_date = query2.end_date,
                            marks = query2.marks,
                            )
                            queryset3.update({'classname':classname,'student_id':student.id,'status':query.status})
                            result.append(queryset3)
                            

                    return Response(result)

                
        elif usertype[0].user_type == 'T':
            
            teacher_id = request.user.id
            # print(teacher_id)
            queryset = AssignClasswiseTeacher.objects.filter(teacher_id=teacher_id,deleted_at=None,status=1).values('available_class_id')
            if queryset:
                
                for i in range(queryset.count()):
                    classes = Classes.objects.filter(id=queryset[i]['available_class_id'])
                    
                    classid = classes[i].id
                    classname = classes[0].classname
                    
                    queryset2 = Assignment.objects.filter(Q(class_division=classid) & Q(deleted_at=None) & ~Q(status = 0))
                    if(queryset2):
                         
                        students = Student.objects.filter(Q(myclass = classid) &Q(deleted_at=None) & Q(status = 1))
                        print(students)
                       
                        if not (students):
                            message = "Students not assigned in this class"
                            return Response({'message':message})

                        
                        
                    result = []
                    for student in students:

                        user_info = Student.objects.get(id = student.id)
                        user_id = user_info.user_id
                        stu_info = Users.objects.filter(id = user_id)
                        student_name = stu_info[0].full_name
                        student_id = stu_info[0].id
                        queryset = StudentAssignment.objects.filter(student = student_id, deleted_at=None)
                        
                        for query in queryset:
                            queryset2 = Assignment.objects.filter(id = query.assignment_id, deleted_at=None)
                            for query2 in queryset2:
                                queryset3 =  dict(id = query2.id,
                                name = query2.name,
                                description = query2.description,
                                start_date = query2.start_date,
                                end_date = query2.end_date,
                                marks = query2.marks,
                                )
                                queryset3.update({'classname':classname,'student_name': student_name,'student_id':student_id,'status':query.status})
                                result.append(queryset3)
                        
                        
                               
                    return Response(result)








# For change assignment status
class AssignmentActiveStatus(APIView):
    def get(self,request): 
        StudentAssignment.objects.filter(
            assignment_id = request.query_params['assignment_id'],student_id = request.query_params['student_id']).update(status=1)
        return Response()

class AssignmentInActiveStatus(APIView):
    def get(self,request):
        

        StudentAssignment.objects.filter(
            assignment_id = request.query_params['assignment_id'],student_id = request.query_params['student_id']).update(status=0)
        return Response()

class AssignmentInProgressStatus(APIView):
    def get(self,request):
        StudentAssignment.objects.filter(
            assignment_id = request.query_params['assignment_id'],student_id = request.query_params['student_id']).update(status=2)
        return Response()

class AssignmentCompletedStatus(APIView):
    def get(self,request):
        student = StudentAssignment.objects.filter(
            assignment_id = request.query_params['assignment_id'],student_id = request.query_params['student_id']).update(status=3)
        
        return Response()


