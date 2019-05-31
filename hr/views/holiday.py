from shared.views import CURDViewSet
from hr.models import *
from hr.serializers import DesignationSerializer, EmployeeCategorySerializer, HolidaySerializer, \
    LeaveStructureSerializer, LeaveTypeSerializer, LoanTypeSerializer, ShiftSerializer, ShiftAllocationSerializer, \
    WeekOffSerializer
# from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from dashboard.models import *
from rest_framework.response import Response

class HolidayListAPIView(CURDViewSet):
    queryset =Holiday.objects.filter(status=1, deleted_at=None)
    serializer_class = HolidaySerializer
    # permission_classes = (IsAuthenticated,)


