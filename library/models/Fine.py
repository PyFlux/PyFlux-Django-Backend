from django.db import models

from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class FineManager(BaseModelManager):
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


class Fine(BaseModel):
    class Meta:
        db_table = '"library_book_fine"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    name = models.CharField(max_length=255, null=True)
    desc = models.CharField(max_length=255, blank=True, null=True)
    fee = models.BigIntegerField(null=True)
    status = models.SmallIntegerField(default=1)

    columns = ['id','name','status']
    order_columns = ['id','name','status','']

    objects = models.Manager() # The default manager.
    filter_objects = FineManager()