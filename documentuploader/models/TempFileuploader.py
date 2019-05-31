from django.db import models
from django.conf import settings
from django.db.models import Q
from shared.models import BaseModel, BaseModelManager
import datetime
from documentuploader.file_upload import *


class TempFileupload(BaseModel):
    class Meta:
        db_table = '"documentuploader_tempfileuploader"'

    filename = models.CharField(max_length=255, blank=True)
    token = models.CharField(max_length=255, null=True)
    file = models.FileField(upload_to=file_upload)
    order = models.IntegerField(default = 1)
    status = models.SmallIntegerField(default=1)
    

    

    
    
    

   