from shared.models import BaseModel
from django.db import models

class UserAddress(BaseModel):
    class Meta:
        db_table = '"dashboard_user_address"'

    userprofile = models.ForeignKey('UserProfile', related_name="addresses", on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey('systemconfig.CityTown', on_delete=models.CASCADE, null=True)
    district = models.ForeignKey('systemconfig.District', on_delete=models.CASCADE, null=True)
    state = models.ForeignKey('systemconfig.State', on_delete=models.CASCADE, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    # p->Permanent Address, t->Temporary Address, 
    # o->Office Address, h->Home Address
    addresstype = models.CharField(max_length=255, blank=True, null=True)
