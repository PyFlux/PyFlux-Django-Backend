from django.db import models
from shared.models import BaseModel


class EmailConfig(BaseModel):
    class Meta:
        db_table = '"system_config_email_config"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    per_day = models.IntegerField(null=True)
    per_month = models.IntegerField(null=True)
    status = models.SmallIntegerField(default=1)

    columns = ['id','per_day','per_month','status']
    order_columns = ['id','per_day','per_month','status','']
    
   