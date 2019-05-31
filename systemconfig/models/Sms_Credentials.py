from django.db import models
from shared.models import BaseModel

from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class SmsCredentialsManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'name':
                q |= Q(name__icontains=search)
            
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column, request):
        return False

class SmsCredentials(BaseModel):
    class Meta:
        db_table = '"system_config_sms_credentials"'
    # ID = models.IntegerField(null=True)
    name = models.CharField(max_length=255, null=True)
    sender = models.CharField(max_length=6, null=True)
    api_key = models.CharField(max_length=255, null=True)
    request_url = models.CharField(max_length=255, null=True)
    test_status = models.BooleanField(default=True)
    status = models.SmallIntegerField(default=1)
    
    columns = ['id','name','sender','api_key','request_url','status']
    order_columns = ['id','name','sender','api_key','request_url','status','']
    
    
    objects = models.Manager() # The default manager.
    filter_objects = SmsCredentialsManager()