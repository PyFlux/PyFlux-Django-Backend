from django.db import models
from shared.models import BaseModel

class StudentAverageMark(BaseModel):
    """
    Calculate average by celery process and
    save it in this table.
    """
    student = models.ForeignKey('dashboard.Users', on_delete= models.CASCADE)
    academic_class = models.ForeignKey('academics.Classes', on_delete= models.CASCADE)
    academic_year = models.ForeignKey('academics.AcademicYear', on_delete= models.CASCADE)
    average_mark = models.IntegerField(default = 0)
    average_attendence = models.IntegerField(default = 0)
    status = models.SmallIntegerField(default = 1)
