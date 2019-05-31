from django.db import models
from shared.models import BaseModel

class PasscodeVerify(BaseModel):
    mobile = models.BigIntegerField(primary_key=True)
    passcode = models.CharField(max_length = 6,default='000000')
    is_verified = models.BooleanField(default=False)
   