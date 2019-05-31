import django
django.setup() 

from django.template import loader
from django.utils import timezone

from celery import shared_task

from fees.views import FeeHelper
from students.models import Student

from systemconfig.models import Email_Queue, Sms_Queue


def addsms(parents, unpaid_fees, today_date):
    for p in parents:
        if not p.parent_user_prof.personal_mobile_no: continue

        message = 'Fees Due on {date}.\n'.format(date= today_date)

        for fee in unpaid_fees:
            message += '{name} - {amount}Rs\n'.format(name = fee.name,amount = fee.amount)
        Sms_Queue.objects.create(
            message = message,
            mobile_number = p.parent_user_prof.personal_mobile_no,
            status = 0) # please change status to 1 so message will just add to DB


@shared_task
def add_email_sms_to_queue():
    """
    create a scheduled task everyday morning 
    to send email/sms on fee due date
    """
    # get all students
    students = Student.objects.all()

    for student in students:
        # if student is not linked with user
        if not student.user: continue

        parents = student.user.student_parents.all()

        # if student is not linked with parent
        if not parents: continue 

        feehelper = FeeHelper(student)
        unpaid_fees = feehelper.get_unpaid_fees(due_date='today')
        if not unpaid_fees:
            # no fees due today
            continue

        today_date = timezone.localtime(timezone.now()).date()
        d = {'fees': unpaid_fees,'user':student.user, 'today':today_date}

        # save to Email_Queue DB. so that every minute email_users scheduler will send it
        Email_Queue.objects.create(
            subject = 'Vidhyadhan - Fees Due on {date}.'.format(date= today_date),
            message = loader.get_template('email_templates/email_fee_due_notification.html').render(d),
            from_email = 'info@vidhyadhan.in' ,
            recepient_list =','.join([p.user.email for p in parents if p.user.is_verified_email]),
            status = 0
        )


        addsms(parents, unpaid_fees, today_date)