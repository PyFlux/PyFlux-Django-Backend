import django
from datetime import date, datetime

django.setup()

from django.template import loader
from django.utils import timezone

from celery import shared_task

from fees.views import FeeHelper
from students.models import Student

from systemconfig.models import Email_Queue, Sms_Queue


@shared_task
def event_notification_sms():
    """
    create a scheduled task everyday morning 
    to send email/sms on fee due date
    """
    # get all students
    students = Student.objects.filter(status=1, deleted_at=None)

    print(" +++++++++++ Event Notification Process +++++++++++ ")






