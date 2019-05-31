from django.db import models
from shared.models import BaseModel

class Email_Queue(BaseModel):
    class Meta:
         db_table = '"system_config_email_queue"'
    
    user_id = models.IntegerField(null=True)
    subject = models.CharField(max_length=255, null=True)
    message = models.TextField(max_length=255, null=True)
    from_email = models.CharField(max_length=255, null=True)
    recepient_list = models.CharField(max_length=255, null=True)
    attachments = models.CharField(max_length=255, blank=True)
    fail_silently = models.BooleanField(default=True)
    attempts = models.CharField(max_length=255, null=True)
    status = models.SmallIntegerField(default=1)

    
