from shared.views import CURDViewSet
from hr.models import *
from hr.serializers import LeaveApplicationSerializer
from rest_framework.permissions import IsAuthenticated 

from rest_framework.response import Response

class LeaveApplicationListAPIView(CURDViewSet):
    queryset = LeaveApplication.objects.filter(status__gt=0,deleted_at=None)
    serializer_class = LeaveApplicationSerializer
    permission_classes = (IsAuthenticated,)
