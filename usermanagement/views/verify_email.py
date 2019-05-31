"""
A two-step (registration followed by activation) workflow, implemented
by emailing an HMAC-verified timestamped activation token to the user
on signup.

"""

from django.contrib.sites.shortcuts import get_current_site
from django.core import signing
from django.template.loader import render_to_string

from rest_framework.response import Response
from rest_framework.views import APIView

from systemconfig.models import Email_Queue

#from django.contrib.auth import get_user_model
from dashboard.models import Users
from rest_framework.exceptions import APIException
from dashboard.models import SystemSettings

class SendVerificationView(APIView):
    """
    GET: Generate an verification key and email it to the user. 
    """
    def get(self, request, format=None): 
        user = request.user
        verification_key = signing.dumps(
            obj=user.get_username(),
            salt='registration'
        )
        siteurl = SystemSettings.objects.get(key = 'site_url')
        current_site = siteurl.value # 'http://localhost:4200/'
        verification_url = '{0}verifyemail/?key={1}'.format(current_site, verification_key)
        message = render_to_string('email_templates/verify_email.html', {
            'user': user,
            'verification_url': verification_url,
        })
        # message = loader.get_template('email_templates/email_user_creation.html').render({
        #     'user':user,'password':password,})

        obj = Email_Queue(
            # user = request.user,
            status = 0,
            recepient_list = user.email,
            from_email = 'info@pyflux.in',
            subject = 'Pyflux - Verify your email address.',
            message = message
        )    
        obj.save()   
        return Response('success') 

class VerificationError(Exception):
    """
    Base class for registration errors.
    """
    def __init__(self, message, code=None, params=None):
        self.message = message
        self.code = code
        self.params = params

class VerifyEmail(APIView):
    ALREADY_VERIFIED_MESSAGE = 'The email you tried to verify has already been verified.'
    BAD_EMAIL_MESSAGE ='The email you attempted to verfiy is invalid.'
    EXPIRED_MESSAGE = 'This verification key has expired.'
    INVALID_KEY_MESSAGE ='The verification key you provided is invalid.'

    def validate_key(self, activation_key):
        """
        Verify that the key is valid, returning the username if
        valid or raising ``VerificationError`` if not.

        """
        try:
            email = signing.loads(activation_key, salt='registration')
            return email
        except signing.SignatureExpired:
            raise APIException(self.EXPIRED_MESSAGE)
        except signing.BadSignature:
            raise APIException(self.INVALID_KEY_MESSAGE)

    def get_userprofile(self, email):
        """
        Given the verified email, look up and return the
        corresponding user account if it exists, or raising
        ``VerificationError`` if it doesn't.

        """       

        try:
            user = Users.objects.get(email = email)
            prof = user.userprofile
            if prof.is_verified_email:
                raise APIException(self.ALREADY_VERIFIED_MESSAGE)
            return prof
        except Users.DoesNotExist:
            raise APIException(self.BAD_EMAIL_MESSAGE)

    def activate(self, *args, **kwargs):
        username = self.validate_key(kwargs.get('key'))
        prof = self.get_userprofile(username)
        prof.is_verified_email = True
        prof.save()
        return prof

    def get(self, *args, **kwargs):
        """
        The base activation logic; subclasses should leave this method
        alone and implement activate(), which is called from this
        method.

        """
        activated_userprofile = self.activate(*args, **kwargs)
        return Response({'message': 'You have verified your email successfully.'})
