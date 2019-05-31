from shared.views import CURDViewSet
from systemconfig.models import *
from systemconfig.serializers import SmsConfigSerializer
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

class SmsConfigListAPIView(CURDViewSet):
    queryset = SmsConfig.objects.filter(status=1, deleted_at=None)
    serializer_class = SmsConfigSerializer
    # permission_classes = (IsAuthenticated,)