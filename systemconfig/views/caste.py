from shared.views import CURDViewSet
from systemconfig.models import *
from systemconfig.serializers import CasteSerializer
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView


class CasteListAPIView(CURDViewSet):
    queryset = Caste.objects.filter(status=1, deleted_at=None)
    serializer_class = CasteSerializer
    # permission_classes = (IsAuthenticated,)

class GetCastes(APIView):
     '''
     get all classes of teacher

     '''
     def get(self, request, format=None):
        queryset = Caste.objects.filter(religion_id=request.query_params.get('religion')).values()
        return Response(queryset)

