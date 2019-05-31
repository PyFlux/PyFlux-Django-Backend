from django.db import models

from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class CityTownManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'city_name':
                q |= Q(city_name__icontains=search)
            
            if col == 'city_state.state_name':
                q |= Q(city_state__state_name__icontains=search)
            
            if col == 'city_country.country_name':
                q |= Q(city_country__country_name__icontains=search)

            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column, request):
        return False

class CityTown(BaseModel):
    class Meta:
        db_table = '"system_config_citytown"'

    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    city_name = models.CharField(max_length=255, null=True)
    city_state = models.ForeignKey('systemconfig.State', on_delete=models.CASCADE, null=True)
    city_country = models.ForeignKey('systemconfig.Country', on_delete=models.CASCADE, null=True)
    status = models.SmallIntegerField(default=1)

    columns = ['id','city_name','city_state.state_name','city_country.country_name','status']
    order_columns = ['id','city_name','city_state.state_name','city_country.country_name','status','']

    
    objects = models.Manager() # The default manager.
    filter_objects = CityTownManager()

    def __str__(self):
        return "%s" % (self.city_name)