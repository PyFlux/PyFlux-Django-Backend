from shared.views import CURDViewSet
from systemconfig.models import *
from systemconfig.serializers import DistrictSerializer
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

class DistrictListAPIView(CURDViewSet):
    queryset = District.objects.filter(status=1, deleted_at=None)
    serializer_class = DistrictSerializer
    # permission_classes = (IsAuthenticated,)