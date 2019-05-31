from django.db.models import Max
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from django.conf import settings
from utils.models import TaskManagement
# Create your views here.
from utils.serializers import TaskManagementSerializer
from shared.views import CURDViewSet
from dashboard.models import *
from django.db.models import Q

class TaskManagementListAPIView(CURDViewSet):
    queryset = TaskManagement.objects.filter(status__gt=0,deleted_at=None)
    serializer_class = TaskManagementSerializer



class GetTaskUsers(APIView):


     def get(self, request, format=None):

        queryset =  Users.objects.filter(Q(deleted_at=None) & ~Q(user_type = 'S') & ~Q(user_type = 'P'))
        
        user_list = []
        for query in queryset.values():
            query.update({'full_name': query['first_name'] + '  ' +query['last_name'] })
            user_list.append(query)
        
       

        return Response(user_list)

class queryTaskUsersByTerm(APIView):
    """
    For ng select Multiselect Serverside processing
    Query Students by a Term 
    """
    def get(self, request, format=None):
        resp=[]
        q = request.GET.get('term','')
        
        users = Users.objects.filter(Q(deleted_at=None) & ~Q(user_type = 'S') & ~Q(user_type = 'P'))
        if q:            
            users = users.filter(
                Q(id__icontains = q) | Q(first_name__icontains = q))
        
        resp = users[:5].values('id','first_name')
        return Response(resp)


    