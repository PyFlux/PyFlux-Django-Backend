from shared.views import CURDViewSet
from hr.models import LeaveStructure
from hr.serializers import LeaveStructureSerializer 
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView
from rest_framework.response import Response

class LeaveStructureListAPIView(CURDViewSet):
    queryset = LeaveStructure.objects.filter(status=1, deleted_at=None)
    serializer_class = LeaveStructureSerializer
    # permission_classes = (IsAuthenticated,)


