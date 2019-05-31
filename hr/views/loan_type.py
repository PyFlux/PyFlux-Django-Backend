from shared.views import CURDViewSet
from hr.models import *
from hr.serializers import DesignationSerializer, EmployeeCategorySerializer, HolidaySerializer, \
    LeaveStructureSerializer, LeaveTypeSerializer, LoanTypeSerializer, ShiftSerializer, ShiftAllocationSerializer, \
    WeekOffSerializer
# from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from dashboard.models import *
from rest_framework.response import Response

class LoanTypeListAPIView(CURDViewSet):
    queryset = LoanType.objects.filter(status=1, deleted_at=None)
    serializer_class = LoanTypeSerializer
    # permission_classes = (IsAuthenticated,)


