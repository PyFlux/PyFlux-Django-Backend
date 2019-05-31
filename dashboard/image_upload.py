import os
from django.conf import settings
import datetime


def image_upload(instance, filename):
    ext = filename.split('.')[-1]
    now = datetime.datetime.now().strftime('%H:%M:%S')
    filename =  'photo_{}.{}'.format(str(now),ext)
    return os.path.join('user',str(instance.user_id), filename)


