from django.db import models
from django.conf import settings
from django.db.models import Q
from shared.models import BaseModel, BaseModelManager
import datetime
from documentuploader.file_upload import *

class FileuploadManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            

            if col == 'filename':
                q |= Q(filename__icontains=search)
            
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)
    def render_column(self, row, column, request):
        return False
    

    def filter_queryset(self, qs, params): 
 
        qs = qs.filter(Q(from_user = params['request'].user )) | qs.filter(Q(to_user = params['request'].user ))
        # filter_send = request.data.get('filter_send', None)
        filename = params['request'].data.get('filename', None)

        if filename:
            qs = qs.filter(filename = filename)
        
        qs = self.filter_search(qs,params['search'])
        return qs

class Fileupload(BaseModel):
    class Meta:
        db_table = '"documentuploader_fileuploader"'

    file = models.FileField(upload_to=file_upload)
    order = models.IntegerField(default = 1)
    filename = models.CharField(max_length=255, null=True)
    chapter_id = models.ForeignKey('documentuploader.Chapter', on_delete=models.CASCADE, related_name='fileuploadfields', null=True)
    status = models.SmallIntegerField(default=1)

    objects = models.Manager() # The default manager.
    filter_objects = FileuploadManager()
    

    

    
    
    

   