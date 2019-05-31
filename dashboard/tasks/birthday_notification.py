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
def birthday_notification_sms():
    """
    create a scheduled task everyday morning 
    to send email/sms on fee due date
    """
    # get all students
    students = Student.objects.filter(status=1, deleted_at=None)

    print(" +++++++++++ Birthday Notification Process +++++++++++ ")
    today = date.today()

    for student in students:
        # if student is not linked with user
        if not student.user: continue

        parents = student.user.student_parents.all()
        # if student is not linked with parent
        if not parents: continue

        # get dob from user profile & check day and month is today
        user_profile = student.user.userprofile
        parsed = datetime.strptime(str(user_profile.dob), "%Y-%m-%d").date().replace(year=today.year)

        if parsed == today:
            message = "Dear " + student.user.first_name + ", Vidhyadhan wishes you a Very Happy Birthday and a Great Year ahead...!"
            # +++++++ Message For Student +++++++
            if user_profile.personal_mobile_no:
                Sms_Queue.objects.create(
                    message=message,
                    mobile_number=user_profile.personal_mobile_no,
                    status=0)  # please change status to 1 so message will just add to DB
            # +++++++ Message For Parent +++++++
            for p in parents:
                if not p.parent_user_prof.personal_mobile_no: continue
                Sms_Queue.objects.create(
                    message=message,
                    mobile_number=p.parent_user_prof.personal_mobile_no,
                    status=0)  # please change status to 1 so message will just add to DB





