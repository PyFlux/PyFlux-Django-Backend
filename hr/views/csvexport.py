import csv
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from hr.models import Employee


class CsvFileExport(APIView):
    def get_foreignkey(self, obj, field):
        if hasattr(obj,field):
            return getattr(obj, field)
        return ''

    def getfields_test(self, e):
        user = e.user
        # prof = user.userprofile
        fields = [
            # Users
            # -----
            ('id', user.id),
            ('first_name', user.first_name),
            ('last_name', user.last_name),
            ('email', user.email),
        ]
        return fields

    def getfields(self, e):
        user = e.user
        prof = user.userprofile
        fields = [
            # Users
            # -----
            ('id', user.id),
            ('first_name', user.first_name),
            ('last_name', user.last_name),
            ('email', user.email),

            # Student
            # -------
            ('emp_code', e.emp_code),
            ('emp_staff_type', e.emp_staff_type),

            ('emp_attendance_card_id',e.emp_attendance_card_id),
            ('emp_category_id',self.get_foreignkey(e.emp_category_id,'employee_category_name')),
            ('emp_joining_date',e.emp_joining_date),
            ('emp_languages',self.get_foreignkey(e.emp_languages,'language_name')),
            ('emp_bank_account_no',e.emp_bank_account_no),
            ('emp_experience_year',e.emp_experience_year),
            ('emp_experience_month',e.emp_experience_month),
            ('emp_reference',e.emp_reference),
            ('emp_guardian_name',e.emp_guardian_name),
            ('emp_guardian_relation',self.get_foreignkey(e.emp_guardian_relation,'name')),
            ('emp_guardian_occupation',self.get_foreignkey(e.emp_guardian_occupation,'name')),
            ('emp_guardian_qualification',e.emp_guardian_qualification),
            ('emp_guardian_income',e.emp_guardian_income),
            ('emp_guardian_home_address',e.emp_guardian_home_address),
            ('emp_guardian_office_address',e.emp_guardian_office_address),
            ('emp_guardian_mobile_no',e.emp_guardian_mobile_no),
            ('emp_guardian_phone_no',e.emp_guardian_phone_no),
            ('emp_guardian_email_id',e.emp_guardian_email_id),
            ('emp_info_emp_master',e.emp_info_emp_master),
            ('same_address',e.same_address),
            ('status',e.status),
            
            # UserProfile
            # -----------
            ('gender', prof.gender),
            ('dob', prof.dob),
            ('birth_place', prof.birth_place),
            ('maritial_status', prof.maritial_status),
            ('blood_group', prof.blood_group),
            ('qualification', prof.qualification),
            ('hobbies', ','.join([h.name for h in prof.hobbies.all()])),
            ('nationality', self.get_foreignkey(prof.nationality,'nationality_name')),
            ('mother_name', prof.mother_name),
            ('father_name', prof.father_name),
            ('designation', self.get_foreignkey(prof.designation,'emp_designation_name')),
            ('religion', self.get_foreignkey(prof.religion,'religion_name')),
            ('religion_caste', self.get_foreignkey(prof.religion_caste,'name')),
            ('home_mobile_no', prof.home_mobile_no),
            ('personal_mobile_no', prof.personal_mobile_no),
            ('office_mobile_no', prof.office_mobile_no),
            ('permanent_address', prof.permanent_address),
            ('permanent_city', self.get_foreignkey(prof.permanent_city,'city_name')),
            ('permanent_district', self.get_foreignkey(prof.permanent_district,'name')),
            ('permanent_state', self.get_foreignkey(prof.permanent_state,'state_name')),
            ('permanent_zip', prof.permanent_zip),
        ]

        return fields

    def get(self, request, format=None):
        # field_names = [field.name for field in Student._meta.fields]

        response = HttpResponse(content_type='application/csv')
        response['Content-Disposition'] = 'attachment; filename=employees.csv'
        writer = csv.writer(response)
        
        employees = Employee.objects.all()
        for i,employee in enumerate(employees):
            csv_data = self.getfields(employee)

            if i == 0:
                # create headers
                writer.writerow([key for key, value in csv_data])
            
            row = writer.writerow([value for key, value in csv_data])

        return response