from django.db.models import Max
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from django.conf import settings
from utils.models import Feedback
# Create your views here.
from utils.serializers import FeedbackSerializer
from shared.views import CURDViewSet
from dashboard.models import *
from django.db.models import Q
from systemconfig.models import *
from django.template import Context, loader
class FeedbackListAPIView(CURDViewSet):
    queryset = Feedback.objects.filter(status__gt=0,deleted_at=None)
    serializer_class = FeedbackSerializer

    def create(self, request, *args, **kwargs):
        
        Feedback.objects.create(
            name = request.data['name'],
            user_id =  request.data['user'],
            description = request.data.get('description',''),
            email = request.data['email_check'],
            status = request.data['status'])
        
        
        data = request.data
        
        userid = data['user']
        if 'user' in data:

            user_data = Users.objects.filter(id=userid)
            

            if 'email_check' in data:
                recepient_list = ','.join([user.email for user in Users.objects.filter(id=2)])
                from_user = ','.join([user.full_name for user in Users.objects.filter(id=userid)])
                to_user = ','.join([user.full_name for user in Users.objects.filter(id=2)])

                obj = Email_Queue(
                    user_id=request.user.id,
                    status=0,
                    recepient_list=recepient_list,
                    from_email=request.user.email,

                    subject='Pyflux-Feedback ' + ''.join(data['name'].split()[:10]),
                )
                data_details = {'message': data['name'],
                                'from_email': request.user.email,
                                'recepient_list': recepient_list,
                                'from_user': from_user,
                                'to_user': to_user,
                                'status': 0,
                                }
                obj.message = loader.get_template('email_templates/email_message.html').render(data_details)
                obj.save()

        return Response('test')

    def update(self, request, *args, **kwargs):
        Feedback.objects.filter(pk = request.data['id']).update(
            name = request.data['name'],
            
            user_id = request.data['user'],
            description = request.data['description'],
            email = request.data['email_check'],
            status = request.data['status'])

        data = request.data
        
        userid = data['user']
        if 'user' in data:

            user_data = Users.objects.filter(id=userid)
            

            if 'email_check' in data:
                recepient_list = ','.join([user.email for user in Users.objects.filter(id=2)])
                from_user = ','.join([user.full_name for user in Users.objects.filter(id=userid)])
                to_user = ','.join([user.full_name for user in Users.objects.filter(id=2)])

                obj = Email_Queue(
                    user_id=request.user.id,
                    status=0,
                    recepient_list=recepient_list,
                    from_email=request.user.email,

                    subject='Pyflux-Feedback ' + ''.join(data['name'].split()[:10]),
                )
                data_details = {'message': data['name'],
                                'from_email': request.user.email,
                                'recepient_list': recepient_list,
                                'from_user': from_user,
                                'to_user': to_user,
                                'status': 0,
                                }
                obj.message = loader.get_template('email_templates/email_message.html').render(data_details)
                obj.save()
        
          
        return Response('test')

class Get_Feedback_details(APIView):

    def get(self, request, format=None):
        queryset = Feedback.objects.filter(Q(deleted_at = None)& ~Q(status = 0)& ~Q(status = 2))
        
        results = []
        i = 0
        for query in queryset.values():
      
            username = queryset[i].user.full_name
            query.update({'username':username})
            results.append(query)
            i +=1
            
        return Response(results)




