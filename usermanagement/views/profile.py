from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from shared.views import TimeDelayed_APIView
from usermanagement.serializers import ChangePasswordSerializer, EditUserProfileSerializer
from dashboard.serializers import UserProfilesSerializer, UsersSerializer
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
            # religion
            serializer_copy_data['religion'] = profile.religion.religion_name if profile.religion else ''
            # hobbies
            serializer_copy_data['hobbies'] = ', '.join([h.name for h in profile.hobbies.all()])
            #serializer_copy_data['verified'] = {'email':profile.is_verified_email,'personal_mobile_no': profile.is_verified_mobile},
            resp['userprofile'] = serializer_copy_data

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