from shared.views import TimeDelayed_APIView
from rest_framework.response import Response
from dashboard.models import SystemSettings

class saveGeneralSetting(TimeDelayed_APIView):
    """
    To Save a General Setting.    
    """
    def get(self, request, format=None):

        key = request.GET['key']
        value = request.GET['value']
        if value == 'true':
            value = '1'
        elif value == 'false':
            value = '0'
        obj = SystemSettings.objects.get(key=key)
        obj.value = value
        obj.save()
        print(key,value, obj)
        return Response('success')


class getGeneralSettings(TimeDelayed_APIView):
    """
    To initail General Setting in checkbox
    """
    def get(self, request, format=None):

        print ('inital settings')
        return Response({obj.key: obj.value for obj in SystemSettings.objects.all()})