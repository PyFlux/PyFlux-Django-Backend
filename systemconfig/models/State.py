from django.db import models
from shared.models import BaseModel
from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class StateManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'state_name':
                q |= Q(state_name__icontains=search)
            
            if col == 'state_country.country_name':
                q |= Q(state_country__country_name__icontains=search)
            
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column, request):
        return False

class State(BaseModel):

    class Meta:
        db_table = '"system_config_state"'
        # ordering = ['id']
    
    state_name = models.CharField(max_length=255, null=True)
    state_country = models.ForeignKey('systemconfig.Country', on_delete=models.CASCADE, null=True)
    status = models.SmallIntegerField()


    columns = ['id','state_name','state_country.country_name','status']
    order_columns = ['id','state_name','state_country.country_name','status']
    
    
    objects = models.Manager() # The default manager.
    filter_objects = StateManager()

    def __str__(self):
        return "%s" % (self.state_name)