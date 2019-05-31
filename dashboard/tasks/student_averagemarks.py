import django
django.setup()

from celery import shared_task
import time
from reports.views.students import TermWiseReportViewSet
from dashboard.models import Users, StudentAverageMark
from academics.models import AcademicYear
from academics.models import Attendence, StudentsAttendence
"""
$ ./manage.py shell
>>> from dashboard.tasks import student_averagemarks
>>> student_averagemarks.student_average_task()
"""


def get_averageattendence(user):
    a_year = AcademicYear.objects.get(status =1)
    year = a_year.start_date.year
    attend_count = Attendence.objects.filter(
                    date__year = year,
                    deleted_at = None,
                    ).count()

    absents = StudentsAttendence.objects.filter(
            attendence__date__year = year,
            student = user,
            deleted_at = None,
        ).count()

    presentdays = attend_count - absents
            
    percentage = round((presentdays/attend_count)*100, 1)
    return percentage

def get_averagemarks(user):
    """
    Average Mark out of 100 for current academic year
    """
    termwise = TermWiseReportViewSet()
    (t_graph, m_entries, academicyear) = termwise.get_graphdata(user,user)
    # t_graph --> [['Onam Exam', 62.875], ['Annual Exam', 67.0], ['Christmas', 65.75]]
    l = [m[1] for m in t_graph]
    average = 0
    if l:
        average = round(sum(l) / len(l), 0)
        
    return average

#@shared_task

def student_average_task():
    """
    Save it in seperate table in database
    Student, Class, AcademicYear, MarkAverage
    -------  -----  ------------  -----------
    """
    # time.sleep(1)
    
    for user in Users.objects.all():
        if hasattr(user, 'student'):
            attendence = get_averageattendence(user)
            marks = get_averagemarks(user)
            item, created = StudentAverageMark.objects.get_or_create(
                #student = StudentAverageMark(
                student = user,
                academic_year = AcademicYear.objects.get(status =1),
                defaults={'academic_class':user.student.myclass}
            )

            # item.academic_class = user.student.myclass
            item.average_mark = marks
            item.average_attendence = attendence
            item.save()