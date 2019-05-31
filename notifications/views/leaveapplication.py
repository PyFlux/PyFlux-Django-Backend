from dashboard.models import Users
from students.models import Student;
from rest_framework.views import APIView
from parents.models import Parents
import datetime
from notifications.views.pushnotifications import FCMNotifications
from django.utils.timezone import datetime as dt


class LeavePushNotification(APIView):
   '''
   when leave application status modified notifications for user

   '''
   def notifications(user,status):
        # https://stackoverflow.com/questions/7503241/django-models-selecting-single-field
        users = Users.objects.get(id=user)
        message = 'Leave Application of {} is {}'.format(str(users.full_name),status)
        data = {'title':'Leave Application','body':message,
        'data':{'title':'Leave Application','body':message,'redirect_type':1}}
        if (users.user_type == 'S'):
            parents = Parents.objects.filter(student = users)
            for par in parents: 
                    FCMNotifications.send_notifications(par.user,data)
        else:
            FCMNotifications.send_notifications(users,data)
