from shared.models import BaseModel
from django.db import models
"""
{
    'site_url':         'http://localhost:4200/', 
    'maintenance_mode': '0', # 1 -> maintenance mode active
}
"""
class SystemSettings(BaseModel):
    class Meta:
        db_table = '"dashboard_system_settings"'

    key = models.CharField(max_length=128,unique=True)
    value = models.CharField(max_length=128, blank=True)

    status = models.SmallIntegerField(default = 1)
    columns = ['id','key','value','status']
    order_columns = ['','name','']