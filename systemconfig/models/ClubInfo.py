from django.db import models
from shared.models import BaseModel

levels = (('0','National'),('2','International'),('3','State'),)


class ClubInfo(BaseModel):
    class Meta:
        db_table = '"system_config_clubinfo"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    club_name = models.CharField(max_length=255, null=True)
    club_code = models.IntegerField(null=True)
    alias= models.CharField(max_length=255, null=True)
    
    level = models.CharField(max_length=255, choices=levels, null=True)
    status = models.SmallIntegerField(default=1)

    columns = ['id','country_name','status']
    order_columns = ['id','country_name','status','']

    def __str__(self):
        return "%s" % (self.club_name)
    
