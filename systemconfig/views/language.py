from shared.views import CURDViewSet
from systemconfig.models import *
from systemconfig.serializers import LanguagesSerializer
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

class LanguagesListAPIView(CURDViewSet):
    queryset = Languages.objects.filter(status=1, deleted_at=None)
    serializer_class = LanguagesSerializer
    # permission_classes = (IsAuthenticated,)
