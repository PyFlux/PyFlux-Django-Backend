from shared.views import CURDViewSet
from hr.models import *
from hr.serializers import LeaveReportingSerializer 
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from dashboard.models import *
from rest_framework.response import Response

class LeaveReportingListAPIView(CURDViewSet):
    queryset = LeaveReporting.objects.filter(status=1, deleted_at=None)
    serializer_class = LeaveReportingSerializer
    permission_classes = (IsAuthenticated,)


