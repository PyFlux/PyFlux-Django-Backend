from django.db import models
from django.conf import settings
from django.db.models import Q
from shared.models import BaseModel, BaseModelManager
import datetime



class StudentFileupload(BaseModel):
    class Meta:
        db_table = '"documentuploader_studentfileuploader"'

    chapter = models.ForeignKey('documentuploader.Chapter', on_delete=models.CASCADE,null=True)
    documents = models.ForeignKey('documentuploader.Fileupload', on_delete=models.CASCADE,null=True)
    student = models.ForeignKey('dashboard.Users', on_delete=models.CASCADE,null=True)

    status = models.SmallIntegerField(default=1)
    
   
    

    

    
    
    

   