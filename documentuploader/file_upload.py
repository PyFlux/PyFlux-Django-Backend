import os
from django.conf import settings
import datetime


def file_upload(instance, filename):
    ext = filename.split('.')[-1]
    print(filename)
    # now = datetime.datetime.now().strftime('%H:%M:%S')
    # filename =  'file_{}.{}'.format(str(now),ext)
    
    return os.path.join('chapter',str(instance.order), filename)
