from shared.views import CURDViewSet
from systemconfig.models import *
from systemconfig.serializers import EmailCredentialsSerializer
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

class EmailCredentialsListAPIView(CURDViewSet):
    queryset =EmailCredentials.objects.filter(status=1, deleted_at=None)
    serializer_class =EmailCredentialsSerializer
    # permission_classes = (IsAuthenticated,)