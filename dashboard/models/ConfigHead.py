from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import Q
#django.contrib.auth.models.UserManager()

from shared.models import BaseModel, BaseModelManager

class ConfigHeadManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'status']: continue

            # apply global search to all searchable columns
            q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)

    def filter_queryset(self, qs, params): 
        qs = qs.filter(deleted_at__isnull=True, status =1)
        qs = self.filter_search(qs,params['search'])
        return qs

class ConfigHead(BaseModel):
    class Meta:
        db_table = '"dashboard_ confighead"'
    
    name = models.CharField(max_length=255, null=True)
    status = models.SmallIntegerField(default=1)
    columns = ['id','name','status']
    order_columns = ['','name','status','']

    objects = objects = models.Manager()
    filter_objects = ConfigHeadManager()
    
    
   
   
   