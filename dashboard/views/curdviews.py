# # from rest_framework.permissions import IsAuthenticated
from shared.views import CURDViewSet

from dashboard.models import Roles, UserProfile, UserRoles, Users
from dashboard.serializers import RolesSerializer, UserProfilesSerializer, \
    UserRolesSerializer, UsersSerializer
from systemconfig.models import Email_Queue 
from django.template import Context,loader
from rest_framework.response import Response
from rest_framework import status

class RolesListAPIView(CURDViewSet):
    queryset = Roles.objects.filter(status=1, deleted_at=None)
    serializer_class = RolesSerializer
   
    def get_queryset(self):
        queryset = super().get_queryset()
        if hasattr(self.request.user, 'userroles'):
            """
            Don't show Roles less than that of authenticated user
            """
            role = self.request.user.userroles.role
            return queryset.filter(id__gte=role.id).order_by('id')
        return queryset.order_by('id')


class UserProfilesListAPIView(CURDViewSet):
    queryset = UserProfile.objects.filter(status=1, deleted_at=None)
    serializer_class = UserProfilesSerializer


class UserRolesListAPIView(CURDViewSet):
    queryset = UserRoles.objects.filter(status=1, deleted_at=None)
    serializer_class = UserRolesSerializer



class UsersListAPIView(CURDViewSet):
    queryset = Users.objects.filter(status=1, deleted_at=None)
    serializer_class = UsersSerializer
   

    def create(self, request, *args, **kwargs):

        
        # ++++++++++  Code for Saving Student Model  ++++++++++++++++++
        userserializer = UsersSerializer(data=request.data)
        if not(userserializer.is_valid()):
            return Response(userserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            userserializer.save()

          # code for sending email to Parent
        pswd = request.data['password']

        message = "Your Pyflux account has been created successfully"
        recepient_list =  Users.objects.get(id = userserializer.data['id']).email
        user =  Users.objects.get(id =userserializer.data['id'])
        obj = Email_Queue(
            user_id = request.user.id,
            status=0,
            recepient_list = recepient_list,
            from_email = 'info@pyflux.in',
            subject = 'Pyflux- '+' '.join(message.split()[:10]),
        )
        data_details = {'user':user,
        'from_email':request.user.email,
        'recepient_list':recepient_list,
        'status':0,
        'password':pswd,
        }
                        
        obj.message = loader.get_template('email_templates/email_user_creation.html').render(data_details)
    
        obj.save()   
        return Response('success')