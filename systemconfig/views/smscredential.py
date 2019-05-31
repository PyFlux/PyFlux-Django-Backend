from shared.views import CURDViewSet
from systemconfig.models import *
from systemconfig.serializers import SmsCredentialsSerializer
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

class SmsCredentialsListAPIView(CURDViewSet):
    queryset = SmsCredentials.objects.filter(status=1, deleted_at=None)
    serializer_class = SmsCredentialsSerializer
    # permission_classes = (IsAuthenticated,)