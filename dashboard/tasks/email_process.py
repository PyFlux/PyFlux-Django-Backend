import django
django.setup() # https://stackoverflow.com/a/39676979/2351696
import os

from django.core import mail

from celery import shared_task

from systemconfig.models import Email_Queue,EmailCredentials
from pathlib import Path    

def get_email_connection():
    """    
    # vidhyahdan
    EmailCredentials(
        smtp_hostname = 'donams.com',
        smtp_port = '587',
        smtp_user_name = 'info@pyflux.in',
        smtp_password = 'InfoPyflux@123#',
        status = 1
    )
    
    # suhailvs@gmail.com
    EmailCredentials(
        smtp_hostname = 'smtp.gmail.com',
        smtp_port = '587',
        smtp_user_name = 'suhailvs@gmail.com',
        smtp_password = 'fhrtaonyhedwowua',
        status = 1
    )
    smtp_hostname = 'smtp.gmail.com'
    smtp_port = '587'
    smtp_user_name = 'pyfluxerp@gmail.com'
    smtp_password = 'xddqenjqfvnrirqy'
    """

    credentials = EmailCredentials.objects.filter(status = 1)[0]

    return mail.get_connection(
        host = credentials.smtp_hostname,
        port = credentials.smtp_port,
        username = credentials.smtp_user_name,
        password = credentials.smtp_password,
        use_tls = True)  


@shared_task
def email_users():
    """
    Send emails in the Email_Queue Table
    """
    connection = get_email_connection()
    connection.open()
    emails = Email_Queue.objects.filter(status = 0)[:100] # first hundred
    email_list = []
    for email in emails:
        # check if email is activate?
        new_email = mail.EmailMessage(email.subject, email.message, to=email.recepient_list.split(','), from_email=email.from_email)
        new_email.content_subtype = "html"
        
        for fp in email.attachments.split(','):
            if fp:
                attachment = open(fp, 'rb')
                new_email.attach(Path(fp).name, attachment.read(),'application/pdf')
                # delete file after sending email https://stackoverflow.com/a/7848959/2351696
                os.unlink(attachment.name) 

        email_list.append(new_email)
        email.status = 1
        email.save()
        
    connection.send_messages(email_list)
    connection.close()
