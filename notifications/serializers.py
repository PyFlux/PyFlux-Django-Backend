from rest_framework import serializers
from notifications.models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    from_user_fullname =  serializers.ReadOnlyField(source='from_user.full_name')
    to_user_fullname =  serializers.ReadOnlyField(source='to_user.full_name')
   
    class Meta:
        model = Notification
        fields = "__all__"  