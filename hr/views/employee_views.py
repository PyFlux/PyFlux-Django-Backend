from shared.views import CURDViewSet
from hr.models import *
from dashboard.models import *
from hr.serializers import EmployeeMasterSerializer, EmployeeSerializer
from dashboard.serializers import UserProfilesSerializer, UsersSerializer, UserRolesSerializer
# from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework.views import APIView
from backend import settings
import os
import datetime
from rest_framework import status
from systemconfig.models import Email_Queue
from django.template import Context,loader
from parents.views import saveaddress
   
class EmployeeListAPIView(CURDViewSet):
    queryset = Employee.objects.filter(status=1, deleted_at=None)
    serializer_class =EmployeeSerializer
    # permission_classes = (IsAuthenticated,)

class EmployeeMasterListAPIView(CURDViewSet):
    queryset = EmployeeMaster.objects.filter(status=1, deleted_at=None).order_by("-id")
    serializer_class =EmployeeMasterSerializer
    # permission_classes = (IsAuthenticated,)


    def create(self, request, *args, **kwargs):
        employee = request.data['emp_details']
        employeeserializer = EmployeeSerializer(data=employee)
        if not(employeeserializer.is_valid()):
            if(Employee.objects.filter(emp_code=employee['emp_code'])):
                return Response({'message':'Employee Code already exist..!'},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(employeeserializer.errors, status=status.HTTP_400_BAD_REQUEST)
                # return Response({'message':'Check the form again'},status=status.HTTP_400_BAD_REQUEST)

        staff_type = request.data['emp_details'].get('emp_staff_type','')
        datejoined = datetime.datetime.now()
        dob = request.data['emp_user_prof']['dob']
        d = datetime.datetime.strptime(str(dob), '%Y-%m-%d')
        pswd = datetime.date.strftime(d, "%d/%m/%Y")
        username = request.data['emp_user']['email']
        emp_user_data = {"is_staff": True, "is_active": True, "is_superuser": False, "date_joined": datejoined, 
        "username":username, "password": pswd, "status": 1,"user_type": staff_type }

        emp_user_data.update(request.data['emp_user'])

        if staff_type == 'T':
            role=8
            
            
        elif staff_type == 'E':
            role=7         
            

        elif staff_type == 'PR':
            role=3 
            

        elif staff_type == 'MN':
            role=6 
            
            
        userserializer = UsersSerializer(data=emp_user_data)
        if not(userserializer.is_valid()):
            if(Users.objects.filter(email=emp_user_data['email'])):
                return Response({'message':'Email already exist..!'},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(userserializer.errors, status=status.HTTP_400_BAD_REQUEST)
                # return Response({'message':'Check the form again'},status=status.HTTP_400_BAD_REQUEST)

        sameaddress = request.data['emp_details'].get('same_address','')
        emp_user_prof = request.data['emp_user_prof']
        # if sameaddress == True:
        #     emp_user_prof["temp_address"] = request.data['emp_user_prof']['permanent_address']
        #     emp_user_prof["temp_zip"] = request.data['emp_user_prof']['permanent_zip']
        #     emp_user_prof["temp_city"] = request.data['emp_user_prof']['permanent_city']
        #     emp_user_prof["temp_district"] = request.data['emp_user_prof']['permanent_district']
        #     emp_user_prof["temp_state"] = request.data['emp_user_prof']['permanent_state']
        
        if emp_user_prof.get('media','') == None:
            emp_user_prof.pop('media')

        userprofserializer = UserProfilesSerializer(data=emp_user_prof)
        if not(userprofserializer.is_valid()): 
            return Response(userprofserializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # return Response({'message':'Check the form again'},status=status.HTTP_400_BAD_REQUEST)
        
        
        userserializer.save()
        employee.update({"user": userserializer.data['id']})
        emp_user_prof.update({"user": userserializer.data['id']})

        employeeserializer = EmployeeSerializer(data=employee)
        
        if employeeserializer.is_valid():
            employeeserializer.save()
        else:
            # return Response({'message':'Check the form again'},status=status.HTTP_400_BAD_REQUEST)
            return Response(employeeserializer.errors, status=status.HTTP_400_BAD_REQUEST)

        userprofserializer = UserProfilesSerializer(data=emp_user_prof)
        
        if userprofserializer.is_valid():
            userprofserializer.save()
        else:
            # return Response({'message':'Check the form again'},status=status.HTTP_400_BAD_REQUEST)
            return Response(userprofserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        saveaddress.save_address(userprofserializer.data['id'], request.data['addresses'])

        # ++++++++++  Code for Saving Employee Role ++++++++++++++++++
        user_roles = {"status": 1,"role":role, "user":userserializer.data['id']}
        emp_user_roleserializer = UserRolesSerializer(data=user_roles)
        if emp_user_roleserializer.is_valid():
            emp_user_roleserializer.save()
        else:
            return Response(emp_user_roleserializer.errors, status=status.HTTP_400_BAD_REQUEST)

        emp_master_data = {"emp_details": employeeserializer.data['id'], "emp_user_prof": userprofserializer.data['id'], "emp_user": userserializer.data['id']}
        empmastererializer = EmployeeMasterSerializer(data=emp_master_data)
        if empmastererializer.is_valid():
            empmastererializer.save()
        else:
            return Response(empmastererializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # return Response({'message':'Check the form again'},status=status.HTTP_400_BAD_REQUEST)
        
         # code for sending email to employee on user creation

        message = "Your Vidhyadhan account has been created successfully"
        recepient_list =  Users.objects.get(id =userserializer.data['id']).email
        user =  Users.objects.get(id =userserializer.data['id'])
        obj = Email_Queue(
            user_id = request.user.id,
            status=0,
            recepient_list = recepient_list,
            from_email = 'info@vidhyadhan.in',
            subject = 'Vidhyadhan- '+' '.join(message.split()[:10]),
        )
        data_details = {'user':user,
        'from_email':request.user.email,
        'recepient_list':recepient_list,
        'status':0,
        'password':pswd,
        }
                        
        obj.message = loader.get_template('email_templates/email_user_creation.html').render(data_details)
    
        obj.save()   

        return Response('success')

    def update(self, request, *args, **kwargs):
        employee_data = request.data['emp_details']
        employee = Employee.objects.get(id=employee_data['id'])
        employeeserializer = EmployeeSerializer(employee, data=employee_data)
        if not(employeeserializer.is_valid()):
            if(Employee.objects.filter(emp_code=employee_data['emp_code'])):
                return Response({'message':'Employee Code already exist..!'},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message':'Check the form again'},status=status.HTTP_400_BAD_REQUEST)

        staff_type = request.data['emp_details'].get('emp_staff_type','')
        dob = request.data['emp_user_prof']['dob']
        d = datetime.datetime.strptime(str(dob), '%Y-%m-%d')
        pswd = datetime.date.strftime(d, "%d/%m/%Y")
        username = request.data['emp_user']['email']
        
        emp_user_data = request.data['emp_user']
        emp_user_data["user_type"] = staff_type 
        emp_user_data["is_staff"] = True 
        emp_user_data["is_active"] = True 
        emp_user_data["is_superuser"] = False 
        emp_user_data["username"] = request.data['emp_user']['email'] 
        emp_user_data["password"] = pswd 
        emp_user_data["status"] = 1 
        
        emp_user_name_same = (str(emp_user_data["username"]) == str(employee.user.username))
        
        if staff_type == 'T':
            role=8
            # emp_user_data["role"] = 8
            
        elif staff_type == 'E':
            role=7         
            # emp_user_data["role"] = 7 

        elif staff_type == 'PR':
            role=3 
            # emp_user_data["role"] = 3 

        elif staff_type == 'MN':
            role=6 
            # emp_user_data["role"] = 6 

        userserializer = UsersSerializer(employee.user,data=emp_user_data)
        if userserializer.is_valid():
            userserializer.save()
        else:
            if(Users.objects.filter(email=emp_user_data['email'])):
                return Response({'message':'Email already exist..!'},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message':'Check the form again'},status=status.HTTP_400_BAD_REQUEST)
        
         # ++++++++++  Code for Saving Employee Role ++++++++++++++++++
        user=userserializer.data['id']
        UserRoles.objects.filter(user=employee.user).update( 
            status=1,
            role=role)
 
        sameaddress = request.data['emp_details'].get('same_address','')
        emp_user_prof = request.data['emp_user_prof']
        # if sameaddress == True:
        #     tempaddress = request.data['emp_user_prof']['permanent_address']
        #     tempZip = request.data['emp_user_prof']['permanent_zip']
        #     tempcity = request.data['emp_user_prof']['permanent_city']
        #     tempdistrict = request.data['emp_user_prof']['permanent_district']
        #     tempstate = request.data['emp_user_prof']['permanent_state']
        # else:
        #     tempaddress = request.data['emp_user_prof']['temp_address']
        #     tempZip = request.data['emp_user_prof']['temp_zip']
        #     tempcity = request.data['emp_user_prof']['temp_city']
        #     tempdistrict = request.data['emp_user_prof']['temp_district']
        #     tempstate = request.data['emp_user_prof']['temp_state']
        user_data =request.data['emp_user_prof']
        userprofile = UserProfile.objects.get(user=employee.user)
        emp_password_same = (str(user_data['dob']) == str(userprofile.dob))

        if(user_data['media']==None):
            # emp_user = UserProfile.objects.get(user=employee.user)
            UserProfile.objects.filter(user=employee.user).update(
                title = user_data['title'],
                # temp_address = tempaddress,
                # temp_zip = tempZip,
                # permanent_address = user_data['permanent_address'],
                # permanent_zip = user_data['permanent_zip'],
                # office_address = user_data['office_address'],
                # office_zip = user_data['office_zip'],
                gender = user_data['gender'],
                dob = user_data['dob'],
                birth_place = user_data['birth_place'],
                maritial_status = user_data['maritial_status'],
                blood_group = user_data['blood_group'],
                qualification = user_data['qualification'],
                qualification_specialization = user_data['qualification_specialization'],
                # adhar_no = user_data['adhar_no'],
                personal_mobile_no = user_data['personal_mobile_no'],
                # temp_city_id = tempcity,
                # temp_district_id =tempdistrict,
                # temp_state_id=tempstate,
                # permanent_city_id=user_data['permanent_city'],
                # permanent_district_id=user_data['permanent_district'],
                # permanent_state_id=user_data['permanent_state'],
                designation_id=user_data['designation'],
                religion_id=user_data['religion'],
                religion_caste_id=request.data['emp_user_prof'].get('religion_caste','')
                )
            for hobby in user_data['hobbies']:
                userprofile.hobbies.add(hobby)

        else:
            emp_photo=UserProfile.objects.filter(user=employee.user).values('media')
            filename=emp_photo[0]['media']
            # used --> https://stackoverflow.com/a/12058684/2351696
            # if(filename):
            #     path = settings.MEDIA_ROOT
            #     if os.path.exists(os.path.join(path, filename)):
            #         os.remove(os.path.join(path, filename))
            #     else:
            #         print("Sorry, I can not remove %s file." % filename)
            if sameaddress == True:
                # emp_user_prof["temp_address"] = request.data['emp_user_prof']['permanent_address']
                # emp_user_prof["temp_zip"] = request.data['emp_user_prof']['permanent_zip']
                # emp_user_prof["temp_city"] = request.data['emp_user_prof']['permanent_city']
                # emp_user_prof["temp_district"] = request.data['emp_user_prof']['permanent_district']
                # emp_user_prof["temp_state"] = request.data['emp_user_prof']['permanent_state']
                emp_user_prof =request.data['emp_user_prof']
            userprofserializer = UserProfilesSerializer(userprofile,data=emp_user_prof)
            if not(userprofserializer.is_valid()):
                return Response(userprofserializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                 userprofserializer.save()
        
        saveaddress.save_address(userprofile.id, request.data['addresses'])
        
        employeeserializer.save()

        # code for sending email to parent if there updation in their username/password
        # code for sending email to employee on user creation
        if emp_user_name_same == False or emp_password_same == False:
            message = "Your Vidhyadhan account has been created successfully"
            recepient_list =  Users.objects.get(id =userserializer.data['id']).email
            user =  Users.objects.get(id =userserializer.data['id'])
            obj = Email_Queue(
                user_id = request.user.id,
                status=0,
                recepient_list = recepient_list,
                from_email = 'info@vidhyadhan.in',
                subject = 'Vidhyadhan- '+' '.join(message.split()[:10]),
            )
            data_details = {'user':user,
            'from_email':request.user.email,
            'recepient_list':recepient_list,
            'status':0,
            'password':pswd,
            }
                            
            obj.message = loader.get_template('email_templates/email_user_creation.html').render(data_details)
        
            obj.save()   

        return Response('success')

class getEmployeeMaster(APIView):
    def get(self, request, format=None):
        queryset = EmployeeMaster.objects.filter(id=request.query_params['id']).values('emp_details_id',
            'emp_user_id', 'emp_user_prof_id')
        employeeserializer = EmployeeSerializer(Employee.objects.get(id=queryset[0]['emp_details_id']))
        empuserserializer = UsersSerializer(Users.objects.get(id=queryset[0]['emp_user_id']))
        empuserprofserializer = UserProfilesSerializer(UserProfile.objects.get(id=queryset[0]['emp_user_prof_id']), context={'request': request})
        return Response({'emp_userprof':empuserprofserializer.data, 'emp_data':employeeserializer.data, 'emp_user':empuserserializer.data})


class GetTeachername(APIView):


     def get(self, request, format=None):

        queryset =  Users.objects.all(user_type = 'T')
        user_list = []
        for query in queryset.values():
            query.update({'full_name': query['first_name'] + '  ' +query['last_name'] })
            user_list.append(query)
        
        # users = Users.objects.annotate(full_name=Concat('first_name', V(' '), 'last_name'))
               
        # print(queryset.values('first_name'))
        # print(users)

        return Response(user_list)
        