"""
+ Create a Django model that stores a user's number and a generated passcode
+ When a new user is created, take their number and SMS them the code
+ When they enter the passcode you sent them, cross reference it with the one stored in the database.
+ If the number is right: verify them, if not, tell them it is wrong and offer to send them an SMS again.
"""
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from systemconfig.models import Sms_Queue
from usermanagement.models import PasscodeVerify
from dashboard.models import UserProfile

class SendVerificationView(APIView):
    def post(self, request, format=None):
        # print (request.data)
        mobile = request.data['mobile']
        # validate = re.search('^[789]\d{9}$', mobile)
        # if validate is None:
        #     return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

        pl = random.sample(range(10),6)
        passcode = ''.join(str(p) for p in pl)

        passcode_entry, created = PasscodeVerify.objects.update_or_create(
            mobile=mobile,  defaults={'passcode' : passcode,'is_verified' : False})

        obj = Sms_Queue(
            # user = request.user,
            status = 0,
            message = "Vidhaydhan - OTP for mobile number verification is {0}".format(passcode), # it is valid upto xxx
            mobile_number = mobile
        )
        obj.save()
        return Response('success')

class VerifyMobile(APIView):
    def post(self, request):
        response_data = {'code' : 'Invalid mobile/OTP' }
        try:
            mobile = request.data['mobile']
            passcode = request.data['otp']
            userprofileid = request.data['userprofileid']
        except:
            return Response(response_data,status=status.HTTP_400_BAD_REQUEST)

        try:
            valid = PasscodeVerify.objects.get(mobile = mobile, passcode = passcode, is_verified = False)
        except PasscodeVerify.DoesNotExist:
            response_data['code'] = 'The OTP you provided is invalid.'
            return Response(response_data,status=status.HTTP_400_BAD_REQUEST)
        # response_data['passcode'] = passcode
        profile = UserProfile.objects.get(id = userprofileid, personal_mobile_no=mobile)
        profile.is_verified_mobile = True
        profile.save()
        response_data['code'] = 'Success'
            
        # SMS api to send passcode
        return Response(response_data, status = status.HTTP_201_CREATED)

