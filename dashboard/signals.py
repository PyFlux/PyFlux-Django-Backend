from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from systemconfig.models import Email_Queue
# from django.template.loader import get_template
from django.template import loader

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_user_email_info(sender, instance, created, **kwargs):
#     if created:
#         # user=instance
#         d = {'site_url': 'http://dev.pyflux.in','user':instance}
#         Email_Queue.objects.create(
#             subject = 'Pyflux - Your account has been created successfully.',
#             message = loader.get_template('email_templates/email_user_creation.html').render(d),
#             from_email = 'info@pyflux.in' ,
#             recepient_list = instance.email,
#             status = 0
#             )
