from rest_framework.response import Response
from rest_framework.views import APIView
from notifications.models import Notification
from notifications.serializers import NotificationSerializer

class NotificationView(APIView):
    """
    Get Notifications of a user
    """
    def get(self, request):
        # otheruser = request.GET['otheruser']
        n = request.GET['n']
        notifications = Notification.objects.filter(
            to_user = request.user
        ).order_by('-created_at')
        if n != 'all':
            # if show 10 item on top nav bar
            notifications = notifications[:int(n)]
        unreadcount = Notification.objects.filter(
            to_user = request.user, 
            read_status = 0
        ).count()
        serializer = NotificationSerializer(notifications, many=True)
        return Response({'notifications':serializer.data, 'unreadcount': unreadcount})

    def post(self, request):
        """
        Mark Notifications as Read
        """
        # user = request.data['user']
        unreadcount = Notification.objects.filter(
            to_user = request.user, 
            read_status = 0
        ).update(read_status=1)
        return Response('success')