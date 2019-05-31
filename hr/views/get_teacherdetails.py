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
from dashboard.models import Users
from hr.models import EmployeeMaster
class Get_TeachersDetails(APIView):
     '''
     get all teachers from user

     '''
     def get(self, request, format=None):
        # queryset = Users.objects.filter(user_type='T', status=1, deleted_at=None).values()
        # print(queryset)
        queryset = EmployeeMaster.objects.filter().values()
        print(queryset)
        return Response(queryset)