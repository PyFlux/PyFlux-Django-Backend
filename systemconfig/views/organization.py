from shared.views import CURDViewSet
from systemconfig.models import *
from systemconfig.serializers import OrganizationSerializer
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

class OrganizationListAPIView(CURDViewSet):
    queryset = Organization.objects.filter(status=1, deleted_at=None)
    serializer_class = OrganizationSerializer
    # permission_classes = (IsAuthenticated,)

class GetActiveOrganization(APIView):
    """
    View Organization in which status is active
    """
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        queryset = OrganizationSerializer(Organization.objects.filter(status = 1, deleted_at  = None),many=True, context={'request': request})
        return Response(queryset.data)
