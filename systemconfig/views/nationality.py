from shared.views import CURDViewSet
from systemconfig.models import *
from systemconfig.serializers import NationalitySerializer
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

class NationalityListAPIView(CURDViewSet):
    queryset = Nationality.objects.filter(status=1, deleted_at=None)
    serializer_class = NationalitySerializer
    # permission_classes = (IsAuthenticated,)
