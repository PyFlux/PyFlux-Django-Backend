from shared.views import CURDViewSet
from hr.models import *

from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from dashboard.models import *
from rest_framework.response import Response


class GetRoles(APIView):
     '''
     get roles

     '''
     def get(self, request, format=None):
        queryset = Roles.objects.filter(status=1, deleted_at=None).values()
        # print(queryset)
        return Response(queryset)



