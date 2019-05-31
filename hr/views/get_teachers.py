from shared.views import CURDViewSet
from hr.models import *

# from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from dashboard.models import *
from rest_framework.response import Response


class GetUser_Teachers(APIView):
     '''
     get all teachers from user

     '''
     def get(self, request, format=None):
        queryset = Users.objects.filter(user_type='T', status=1, deleted_at=None).values()
        return Response(queryset)



