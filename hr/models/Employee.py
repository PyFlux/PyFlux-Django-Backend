from django.db import models
from shared.models import BaseModel
from django.conf import settings

class Employee(BaseModel):
    class Meta:
        db_table = '"hr_emp_info"'
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    emp_code = models.CharField(max_length=255, unique=True, null=True)
    emp_staff_type =  models.CharField(max_length=255, null=True)
    emp_attendance_card_id =  models.CharField(max_length=255, null=True)
    emp_category_id = models.ForeignKey('hr.EmployeeCategory', on_delete=models.CASCADE, null=True)
    emp_joining_date = models.DateField(null=True)
    emp_languages = models.ForeignKey('systemconfig.Languages', on_delete=models.CASCADE, null=True)
    emp_bank_account_no = models.CharField(max_length=255, null=True)
    emp_experience_year = models.CharField(max_length=255, null=True, blank=True)
    emp_experience_month = models.CharField(max_length=255, null=True, blank=True)
    emp_reference = models.CharField(max_length=255, null=True, blank=True)
    emp_guardian_name = models.CharField(max_length=255, null=True)
    emp_guardian_relation = models.ForeignKey('systemconfig.Relationship', on_delete=models.CASCADE, null=True)
    emp_guardian_qualification = models.CharField(max_length=255, null=True, blank=True)
    emp_guardian_occupation = models.ForeignKey('systemconfig.Occupation', on_delete=models.CASCADE, null=True)
    emp_guardian_income = models.CharField(max_length=255, null=True, blank=True)
    emp_guardian_home_address = models.CharField(max_length=255, null=True, blank=True)
    emp_guardian_office_address = models.CharField(max_length=255, null=True, blank=True)
    emp_guardian_mobile_no = models.CharField(max_length=255, null=True, blank=True)
    emp_guardian_phone_no = models.CharField(max_length=255, null=True, blank=True)
    emp_guardian_email_id = models.CharField(max_length=255, null=True, blank=True)
    emp_info_emp_master =  models.CharField(max_length=255, null=True)
    same_address = models.BooleanField(default=False)
    status = models.SmallIntegerField(default=1, null=True)


 