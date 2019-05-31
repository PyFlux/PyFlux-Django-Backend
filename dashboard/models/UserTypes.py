from shared.models import BaseModel
from django.db import models

class UserTypes(BaseModel):

    name = models.CharField(max_length=128,unique=True)
    user_type = models.CharField(max_length=128, blank=True)

    status = models.SmallIntegerField(default = 1)
    columns = ['id','name','user_type','status']
    order_columns = ['','name','']