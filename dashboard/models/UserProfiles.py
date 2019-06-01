from shared.models import BaseModel
from django.db import models
from dashboard.image_upload import *
from django.conf import settings

class UserProfile(BaseModel):
    class Meta:
        db_table = '"dashboard_user_profile"'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)

    title = models.CharField(max_length=255, null=True)  # Mr, Mrs
    # address = models.ManyToManyField('UserAddress')

    # temp_address = models.CharField(max_length=255, blank=True, null=True)
    # temp_city = models.ForeignKey('systemconfig.CityTown', related_name='temp_city', on_delete=models.CASCADE, null=True)
    # temp_district = models.ForeignKey('systemconfig.District', related_name='temp_district', on_delete=models.CASCADE, null=True)
    # temp_state = models.ForeignKey('systemconfig.State', related_name='temp_state''', on_delete=models.CASCADE, null=True)
    # temp_zip = models.CharField(max_length=255, blank=True, null=True)

    # permanent_address = models.CharField(max_length=255, blank=True, null=True)
    # permanent_city = models.ForeignKey('systemconfig.CityTown', related_name='permanent_city', on_delete=models.CASCADE, null=True)
    # permanent_district = models.ForeignKey('systemconfig.District', related_name='permanent_district', on_delete=models.CASCADE, null=True)
    # permanent_state = models.ForeignKey('systemconfig.State', related_name='permanent_state', on_delete=models.CASCADE, null=True)
    # permanent_zip = models.CharField(max_length=255, blank=True, null=True)

    # office_address = models.CharField(max_length=255, blank=True, null=True)
    # office_city = models.ForeignKey('systemconfig.CityTown', related_name='office_city', on_delete=models.CASCADE, null=True)
    # office_district = models.ForeignKey('systemconfig.District', related_name='office_district', on_delete=models.CASCADE, null=True)
    # office_state = models.ForeignKey('systemconfig.State', related_name='office_state', on_delete=models.CASCADE, null=True)
    # office_zip = models.CharField(max_length=255, blank=True, null=True)

    gender = models.CharField(max_length=255, blank=True, null=True)  # M - Male, F - Female
    dob = models.DateField(max_length=8, blank=True, null=True)
    birth_place = models.CharField(max_length=255, blank=True, null=True)
    maritial_status = models.CharField(max_length=255, blank=True, null=True)  # 0 - unmarried, 1 - married, 2 - widow
    blood_group = models.CharField(max_length=255, blank=True, null=True)  # A+, B+ etc
    qualification = models.CharField(max_length=255, blank=True, null=True)
    qualification_specialization = models.CharField(max_length=255, blank=True, null=True)
    hobbies = models.ManyToManyField('systemconfig.Hobby', related_name='hobby', blank=True)
    nationality = models.ForeignKey('systemconfig.Nationality', blank=True, on_delete=models.CASCADE, null=True)
    adhar_no = models.CharField(max_length=255, blank=True, null=True)  # In encrypted format

    mother_name = models.CharField(max_length=255, blank=True, null=True)  # In encrypted format
    father_name = models.CharField(max_length=255, blank=True, null=True)  # In encrypted format

    designation = models.CharField(max_length=255, blank=True, null=True)  # Software Engineer
    religion = models.ForeignKey('systemconfig.Religion', on_delete=models.CASCADE, null=True)  # Christian, Hindu etc
    religion_caste = models.ForeignKey('systemconfig.Caste', on_delete=models.CASCADE, blank=True, null=True)  # SC, ST, OBC etc

    home_mobile_no = models.CharField(max_length=255, blank=True, null=True)  # 0487 2557834
    personal_mobile_no = models.CharField(max_length=255, blank=True, null=True)  # 9895 783759
    office_mobile_no = models.CharField(max_length=255, blank=True, null=True)  # 9895 783759

    media = models.ImageField(upload_to=image_upload, blank=True , null=True)  # Image file name from media folder under user id
    

    # whether email and mobile number verified
    is_verified_email = models.BooleanField(default=False)
    is_verified_mobile = models.BooleanField(default=False)
    
    status = models.SmallIntegerField(default=1)  # 0 - Inactive, 1 - Active

    def __str__(self):
        return "%s" % (self.user)
