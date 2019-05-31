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

from fees.models import FeePaymentTransaction

@receiver(post_save, sender=FeePaymentTransaction)
def fee_payment_recipt(sender, instance, created, **kwargs):
    d = {'site_url': 'http://dev.pyflux.in','user':instance.student.user,'fee':instance}
    for parent in instance.student.user.student_parents.all():
        # print(parent.user.email)
        if not parent.user.is_verified_email: 
            continue
        Email_Queue.objects.create(
            subject = 'Fee Transaction for {name}'.format(name =instance.feecategory.name),
            message = loader.get_template('email_templates/email_fee_receipt.html').render(d),
            from_email = 'info@pyflux.in' ,
            recepient_list = parent.user.email,
            status = 0 # is it send?
            )
   
    