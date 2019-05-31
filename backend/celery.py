from celery import Celery
from celery.schedules import crontab
import os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery()
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(['dashboard'])


from dashboard.tasks import (email_process, sms_process, fee_due_notification, 
    birthday_notification, event_notification, student_averagemarks)

from reports.views import pdf

from systemconfig.models import Email_Queue

@app.task
def generate_report(email, markentryid, userid):
    """
    Used by markentry_views --> ListClassStudents & 
    * generate pdf reports after markentry.
    * attach and send email
    """
    email = Email_Queue(
        user_id = email['user_id'],
        status=0,
        recepient_list = email['recepient_list'],
        from_email = email['from_email'],
        subject = email['subject'],
        message = email['message'],
    )
    
    print(markentryid, userid)
    g = pdf.GeneratePDF(m_id = markentryid)
    g.generate(userid) # g.generate(userid)
    print('generated pdf')
    email.attachments = g.get_path(userid)
    email.save()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    # +++++++++++ SMS Process +++++++++++
    sender.add_periodic_task(5, sms_process.sendsms.s(), name='Every 5 seconds')

    # +++++++++++ Email Process +++++++++++
    sender.add_periodic_task(60, email_process.email_users.s(), name='Every 60 seconds')

    # +++++++++++ Fee Due Notification +++++++++++
    # every day at 1:00 a.m.
    sender.add_periodic_task(crontab(hour=1, minute=0), fee_due_notification.add_email_sms_to_queue.s(), name='every day at 1:00 a.m')
    # Testing purpose
    # sender.add_periodic_task(5, fee_due_notification.add_email_sms_to_queue.s(), name='Every 5 seconds')

    # +++++++++++ Birthday Notification +++++++++++
    # every day at 1:00 a.m.
    sender.add_periodic_task(crontab(hour=1, minute=0), birthday_notification.birthday_notification_sms.s(), name='Every day at 1:00 a.m')
    # Testing purpose
    # sender.add_periodic_task(5, birthday_notification.birthday_notification_sms.s(), name='every 5 seconds')

    # ++++++++++++ Calculate average marks ++++++++++++
    # crontab(0, 0, day_of_month='1')
    sender.add_periodic_task(crontab(hour=2, minute=0), student_averagemarks.student_average_task.s(), name='1st of every month')
    
    # +++++++++++ Event Notification +++++++++++
    # every day at 1:00 a.m.
    # sender.add_periodic_task(crontab(hour=1, minute=0), event_notification.event_notification_sms.s(),name='Every day at 1:00 a.m')
    # Testing purpose
    # sender.add_periodic_task(5, event_notification.event_notification_sms.s(), name='every 5 seconds')

    # +++++++++++ Absent Student Notification +++++++++++
    # Moved to absent mark list