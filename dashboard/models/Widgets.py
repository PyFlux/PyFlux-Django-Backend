from django.db import models
# https://stackoverflow.com/q/47486356/2351696
from django.core.validators import validate_comma_separated_integer_list

from shared.models import BaseModel


class Widget(BaseModel):
    # Widgets to be shown in dashboard
    name = models.CharField(max_length=255)
    # eg: profile,fees,events,noticeboard,holidays
    code = models.CharField(max_length=255)
    status = models.SmallIntegerField(default = 1)
    # roleids as csv -> '3,4,5,1'
    roletypes = models.CharField(max_length=200, blank=True, default='')
    columns = ['id','name','code','status']
    order_columns = ['','name','code','']

    def __str__(self):
        return "%s" % (self.name)