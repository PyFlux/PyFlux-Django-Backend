from shared.views import CURDViewSet
from hr.models import *
from hr.serializers import DesignationSerializer
# from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from dashboard.models import *
from rest_framework.response import Response

class DesignationListAPIView(CURDViewSet):
    queryset = Designation.objects.filter(status=1, deleted_at=None)
    serializer_class = DesignationSerializer
    # permission_classes = (IsAuthenticated,)

