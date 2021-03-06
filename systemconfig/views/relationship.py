from shared.views import CURDViewSet
from systemconfig.models import *
from systemconfig.serializers import RelationshipSerializer
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.views import APIView

class RelationshipListAPIView(CURDViewSet):
    queryset = Relationship.objects.filter(status=1, deleted_at=None)
    serializer_class = RelationshipSerializer
    # permission_classes = (IsAuthenticated,)
