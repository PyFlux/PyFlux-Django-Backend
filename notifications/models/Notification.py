from django.db import models
from shared.models import BaseModel,BaseModelManager

class Notification(BaseModel):
    class Meta:
        db_table = '"notification_msg"'
    
    from_user = models.ForeignKey('dashboard.Users', on_delete=models.CASCADE, related_name='notification_from',null=True)
    to_user = models.ForeignKey('dashboard.Users', on_delete=models.CASCADE, related_name='notification_to', null=True)
    message = models.TextField()
    read_status = models.IntegerField(default=0) # 0 unread, 1 read
    read_times = models.IntegerField(default=0)
    status = models.SmallIntegerField(default=1)
    
    

    