# # from rest_framework.permissions import IsAuthenticated
from shared.views import CURDViewSet

from dashboard.models import Roles, UserProfile, UserRoles, Users,ConfigDetail,ConfigHead
from dashboard.serializers import RolesSerializer, UserProfilesSerializer, \
    UserRolesSerializer, UsersSerializer,ConfigDetailSerializer,ConfigHeadSerializer
from systemconfig.models import Email_Queue 
from django.template import Context,loader
from rest_framework.response import Response




class ConfigDetailListAPIView(CURDViewSet):
    queryset = ConfigHead.objects.filter(status=1, deleted_at=None)
    serializer_class = ConfigHeadSerializer
   

   

    