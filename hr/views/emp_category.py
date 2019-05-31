from shared.views import CURDViewSet
from hr.models import *
from hr.serializers import  EmployeeCategorySerializer
# from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from dashboard.models import *
from rest_framework.response import Response

class EmployeeCategoryListAPIView(CURDViewSet):
    queryset =EmployeeCategory.objects.filter(status=1, deleted_at=None)
    serializer_class = EmployeeCategorySerializer
    # permission_classes = (IsAuthenticated,)
