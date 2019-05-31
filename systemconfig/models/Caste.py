from django.db import models

from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class CasteManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue
            
            if col == 'religion.religion_name':
                q |= Q(religion__religion_name__icontains=search)

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

class Caste(BaseModel):

    class Meta:
        db_table = '"system_config_caste"'
    name = models.CharField(max_length=255, null=True)
    religion = models.ForeignKey('systemconfig.Religion', on_delete=models.CASCADE, null=True)
    status = models.SmallIntegerField()


    columns = ['id','religion.religion_name','name','status']
    order_columns = ['id','religion.religion_name','name','status','']
    
    objects = models.Manager() # The default manager.
    filter_objects = CasteManager()

    def __str__(self):
        return "%s" % (self.name)