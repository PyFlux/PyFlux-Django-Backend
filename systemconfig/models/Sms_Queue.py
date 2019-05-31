from django.db import models
from django.conf import settings

from shared.models import BaseModel

class Sms_Queue(BaseModel):
    class Meta:
        db_table = '"system_config_sms_queue"'
    
    # ID = models.AutoField(primary_key=True,max_length=10)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    message = models.TextField(max_length=250, default = '')
    mobile_number = models.CharField(max_length=255,blank=True, default = '')
    submitted_date = models.DateField(null=True, blank=True)
    to_type = models.IntegerField(null=True)
    error_code = models.CharField(max_length=15, blank=True, default = '')
    status = models.SmallIntegerField()

    # columns = ['user','message','mobile_number','submitted_Date','to_type','error_code','status']
    # order_columns = ['','user','message','mobile_number','submitted_date','to_type','error_code','status','']
  