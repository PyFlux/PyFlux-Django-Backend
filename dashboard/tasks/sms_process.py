import django
django.setup()
from celery import shared_task
from systemconfig.models import Sms_Queue,SmsCredentials

import urllib,json

@shared_task
def sendsms():
    """
    apikey = '7sFCiwbkUDo-b5FQLUSKWADY1TOG7XhbnNi5NDE7Zp'
    sender = 'TXTLCL'
    request_url = 'https://api.textlocal.in/send/?'
    https://api.textlocal.in/send/?apikey=7sFCiwbkUDo-b5FQLUSKWADY1TOG7XhbnNi5NDE7Zp&numbers=917356775981&sender=TXTLCL&message=asdasdffjlasfj
    
    SmsCredentials(
        name = 'textlocal',
        sender = 'TXTLCL',
        api_key = '7sFCiwbkUDo-b5FQLUSKWADY1TOG7XhbnNi5NDE7Zp',
        request_url = 'https://api.textlocal.in/send/?',
        status = 1
    )
    """
    cred = SmsCredentials.objects.filter(status = 1)[0]
    sms = Sms_Queue.objects.filter(status = 0, error_code='')[:100] # first hundred
    for item in sms:
        params = {'apikey': cred.api_key, 'numbers': item.mobile_number, 'message' : item.message, 'sender': cred.sender}
        f = urllib.request.urlopen(cred.request_url+ urllib.parse.urlencode(params))
        resp = json.loads(f.read())
        if resp['status'] == 'success':
            item.status = 1
        else:
            item.error_code = resp['errors'][0]['code']
        item.save()
        
        
