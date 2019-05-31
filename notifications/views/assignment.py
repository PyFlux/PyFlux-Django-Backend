from dashboard.models import Users
from students.models import Student;
from rest_framework.views import APIView
from parents.models import Parents
import datetime
from notifications.views.pushnotifications import FCMNotifications
from django.utils.timezone import datetime as dt


class AssignmentPushNotification(APIView):
   '''
   when leave application status modified notifications for user

   '''
   def notifications(myclass):
        # https://stackoverflow.com/questions/7503241/django-models-selecting-single-field
        class_students = list(Student.objects.filter(myclass_id = myclass).values_list('user_id', flat=True))
        
        for stu in class_students:
          users = Users.objects.get(id=stu)
          message = 'New Assignment assigned for {}'.format(str(users.full_name))
          data = {'title':'Assignment','body':message,
          'data':{'title':'Assignment','body':message,'redirect_type':1}}
          if (users.user_type == 'S'):
              parents = Parents.objects.filter(student = users)
              for par in parents: 
                      FCMNotifications.send_notifications(par.user,data)
          # FCMNotifications.send_notifications(users,data)
