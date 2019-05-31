import os
from django.conf import settings
import datetime

def template_upload(instance, filename):
    ext = filename.split('.')[-1]
    now = datetime.datetime.now().strftime('%H:%M:%S')
    filename =  'template_file_{}.{}'.format(str(now),ext)
    return os.path.join('template',  filename)

