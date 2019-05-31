from dashboard.models import *
from rest_framework.views import APIView
from rest_framework.response import Response


class Get_Current_user(APIView):

    def get(self, request, format=None):
        queryset = Users.objects.filter(id=request.user.id, status=1, deleted_at=None).values()
        return Response(queryset)

class Get_users(APIView):

    def get(self, request, format=None):
        queryset = Users.objects.filter(status=1, deleted_at=None).values()
        return Response(queryset)

class Get_Current_username(APIView):

    def get(self, request, format=None):
        queryset = Users.objects.filter(id=request.user.id, status=1, deleted_at=None)
        print(queryset[0].id)
        username = queryset[0].full_name
        userid = queryset[0].id
        results = []

        results.append({'user_id':userid, 'user_name':username})
        # return Response(results)
        print(results)
        return Response(results)

