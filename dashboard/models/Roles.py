from django.db.models import Q
from django.db import models

from shared.models import BaseModel, BaseModelManager

class RolesManager(BaseModelManager):
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
        qs = self.filter_search(qs,params['search'])
        return qs

class Roles(BaseModel):
    role_type = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=128,unique=True)
    widgets = models.ManyToManyField('Widget', blank=True)

    status = models.SmallIntegerField(default = 1)
    columns = ['id','name','status']
    order_columns = ['id','name','status']

    objects = models.Manager() # The default manager.
    filter_objects = RolesManager()
    
    def __str__(self):
        return "%s" % (self.name)
