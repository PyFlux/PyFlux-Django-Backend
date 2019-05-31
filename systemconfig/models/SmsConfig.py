from django.db import models
from shared.models import BaseModel

from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class SmsConfigManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'per_day':
                q |= Q(per_day__icontains=search)
            
            if col == 'per_month':
                q |= Q(per_month__icontains=search)
            
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column, request):
        return False

class SmsConfig(BaseModel):
    class Meta:
        db_table = '"system_config_sms_config"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    # sms_count = models.IntegerField(null=True)
    api_key = models.CharField(max_length=255, null=True)
    status = models.SmallIntegerField(default=1)
    per_day = models.IntegerField(null=True)
    per_month = models.IntegerField(null=True)
    columns = ['id','per_day','per_month','status']
    order_columns = ['id','per_day','per_month','status','']
    
    
    objects = models.Manager() # The default manager.
    filter_objects = SmsConfigManager()