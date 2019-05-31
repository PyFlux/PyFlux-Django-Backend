from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from shared.views import TimeDelayed_APIView
from students.models import StudentSerializer, StudentMasterSerializer, StudentMaster
from usermanagement.serializers import ChangePasswordSerializer, EditUserProfileSerializer
from dashboard.serializers import UserProfilesSerializer, UsersSerializer
from parents.models import Parents
from dashboard.models import UserProfile, UserAddress
from dashboard.serializers import AddressSerializer

class ProfilePage(TimeDelayed_APIView):
    """
    To get Show Profile Page of the loggedin User
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, format=None): 
        # print('-'*100)
        resp = {
            'student':'', 
            'teacher':'',
            'userprofile':'',
            'username':request.user.username,
            'email':request.user.email,
            'full_name': '{0} {1}'.format(request.user.first_name, request.user.last_name),
        } # 
        if hasattr(request.user, 'userprofile'):
            profile = request.user.userprofile
            profile_serializer = UserProfilesSerializer(profile, context={'request': request})
            serializer_copy_data = profile_serializer.data.copy()

            # to get address
            # city
            # serializer_copy_data['temp_city'] = profile.temp_city.city_name if profile.temp_city else ''
            # serializer_copy_data['permanent_city'] = profile.permanent_city.city_name if profile.permanent_city else ''
            # serializer_copy_data['office_city'] = profile.office_city.city_name if profile.office_city else ''
            
            # # district
            # serializer_copy_data['temp_district'] = profile.temp_district.name if profile.temp_district else ''
            # serializer_copy_data['permanent_district'] = profile.permanent_district.name if profile.permanent_district else ''
            # serializer_copy_data['office_district'] = profile.office_district.name if profile.office_district else ''
            
            # # state
            # serializer_copy_data['temp_state'] = profile.temp_state.state_name if profile.temp_state else ''
            # serializer_copy_data['permanent_state'] = profile.permanent_state.state_name if profile.permanent_state else ''
            # serializer_copy_data['office_state'] = profile.office_state.state_name if profile.office_state else ''
            
            # religion
            serializer_copy_data['religion'] = profile.religion.religion_name if profile.religion else ''
            # hobbies
            serializer_copy_data['hobbies'] = ', '.join([h.name for h in profile.hobbies.all()])
            #serializer_copy_data['verified'] = {'email':profile.is_verified_email,'personal_mobile_no': profile.is_verified_mobile},
            
            resp['userprofile'] = serializer_copy_data

        if hasattr(request.user, 'student'):
            serializer = StudentSerializer(request.user.student,context={'request': request})
            resp['student'] = serializer.data

            """
            Datas to show GuardianDetails Tab in student profile page
            """
            guardians = []
            active_parent = StudentMaster.objects.get(stu_user = request.user).parent_details
            for parent in Parents.objects.filter(student = request.user):
                profile = parent.parent_user_prof
                addresses_serializer = AddressSerializer(profile.addresses, many=True)
                guardians.append({
                    'full_name': '{0} {1}'.format(parent.user.first_name, parent.user.last_name),
                    'email': parent.user.email,
                    'media': request.build_absolute_uri(profile.media.url) if profile.media else '',
                    'phone': profile.personal_mobile_no,
                    'addresses':addresses_serializer.data,

                    # 'address': profile.permanent_address,
                    # 'city': profile.permanent_city.city_name,
                    # 'district': profile.permanent_district.name,
                    # 'state': profile.permanent_state.state_name,
                    # 'zip': profile.permanent_zip,
                    'active_parent': parent == active_parent,

                })

            resp['guardians'] = guardians

                    
        if hasattr(request.user, 'parents'):
            """ 
            Datas to show Student Details Tab in parent profile page
            """
            childrens = []
            for child in request.user.parents.student.all():
                childrens.append({
                    'full_name': '{0} {1}'.format(child.first_name, child.last_name),
                    'email': child.email,
                    'media': request.build_absolute_uri(child.userprofile.media.url) if child.userprofile.media else '',
                    'phone': child.userprofile.personal_mobile_no,   
                })

            resp['childrens'] = childrens

        return Response(resp)

    def post(self,request):
        """
        Password change
        """
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            user = request.user
            # Check old password
            old_password = serializer.data.get("old_password")
            if not user.check_password(old_password):
                return Response({"old_password": ["Wrong password."]}, 
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditUserProfile(TimeDelayed_APIView):
    """
    To get Show Profile Page of the loggedin User
    """
    # permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        user = UsersSerializer(request.user)
        userprofile = {}
        if hasattr(request.user,'userprofile'):
            serializer = UserProfilesSerializer(request.user.userprofile, context={'request': request})
            userprofile = serializer.data

        return Response({'userprofile':userprofile,'user':user.data})

    def post(self,request):
        """
        Edit User Profile details
        """
        # on editing userprofile you need to save first_name, last_name and email
        if 'first_name' in request.data:            
            userserializer = UsersSerializer(request.user, data=request.data, partial=True)
            if userserializer.is_valid():
                old_email = request.user.email # if email change, then verify the email again
                userserializer.save()
            else:
                return Response(userserializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        #print(request.data.get('media',''))
        if request.data.get('media','') == None:
            # print('Media is None')
            request.data.pop('media')


        if hasattr(request.user,'userprofile'):
            serializer = UserProfilesSerializer(request.user.userprofile, data=request.data, partial=True, context={'request': request}) #UserProfilesSerializer(data=request.data)
            old_phone = request.user.userprofile.personal_mobile_no

            # save phone and email verified or not
            is_verified_mobile = request.user.userprofile.is_verified_mobile
            is_verified_email = request.user.is_verified_email
        else:
            # UserProfile doesn't exist for the user
            is_verified_mobile = False
            is_verified_email = False

            old_phone = request.data['personal_mobile_no']
            # if user profile doesn't exists, then create a new userprofile.
            extra_data = {"user": request.user.id}
            extra_data.update(request.data)
            serializer = UserProfilesSerializer(data=extra_data, partial=True, context={'request': request}) #UserProfilesSerializer(data=request.data)
        
        if serializer.is_valid():
            if old_email != request.data['email']:
                # if user changed his email
                is_verified_email = False

            if old_phone != request.data['personal_mobile_no']:
                # if user changed mobile
                is_verified_mobile = False
            
            serializer.save(is_verified_email = is_verified_email, is_verified_mobile = is_verified_mobile )

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditUserAddress(TimeDelayed_APIView):
    def post(self,request):
        """
        Edit User Address
        """
        # {'addresses': [
        #     {'address': 'gafdsaf asdf', 'city': '1', 'district': '2', 
        # 'state': '3', 'zipcode': 234242, 'addresstype': None}
        # ]}
        UserAddress.objects.filter(userprofile_id=request.data['userprofile']).delete()
        for address in request.data['addresses']:
            # UserAddress.objects.create(**address)
            UserAddress.objects.create(
                userprofile_id = request.data['userprofile'],
                address = address['address'],
                city_id = address['city'],
                district_id = address['district'],
                state_id = address['state'],
                zipcode = address['zipcode'],
                addresstype = address['addresstype']
            )
                
        # print(request.data)
        return Response(request.data)

class GetUserProfile(TimeDelayed_APIView):
     '''
     get current users profile data

     '''
     def get(self, request, format=None):
        queryset = UserProfilesSerializer(UserProfile.objects.filter(user_id = request.user.id),many=True, context={'request': request})
        return Response(queryset.data)