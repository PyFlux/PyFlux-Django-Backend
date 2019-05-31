from rest_framework.response import Response
from rest_framework.views import APIView
from dashboard.sync_dashboard_menu import add_dashboard_menu
import json

class SyncMenus(APIView):
    """
    Synchronize Dashboard Menus
    """
    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.data['menus'])
        add_dashboard_menu(json_data)
        # print (json_data)
        return Response('success')