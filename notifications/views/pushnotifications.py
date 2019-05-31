# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.timezone import datetime
from fcm_django.models import FCMDevice

class FCMNotifications(APIView):

#### code For Sending Push Notifications ####
    def send_notifications(user,message):
        # print(message)
        devices = FCMDevice.objects.filter(user=user).first()
        if devices:
            devices.send_message(title=message['title'],
             body=message['body'], data = message['data'])
            # devices.send_message(title="Title", body="Message", data={"test": "test"})