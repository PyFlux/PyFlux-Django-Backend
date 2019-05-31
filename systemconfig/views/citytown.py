from shared.views import CURDViewSet
from systemconfig.models import *
from systemconfig.serializers import CityTownSerializer
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class CityTownListAPIView(CURDViewSet):
    queryset = CityTown.objects.filter(status=1, deleted_at=None)
    serializer_class = CityTownSerializer
    # permission_classes = (IsAuthenticated,)