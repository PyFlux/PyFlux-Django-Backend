from django.db import models
from django.conf import settings
from django.db.models import Q
from shared.models import BaseModel, BaseModelManager
import datetime

class ModuleManager(BaseModelManager):   

    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status','myclass.classname']: continue

            if col == 'category':
                q |= Q(category__icontains=search)
            if col == 'description':
                q |= Q(description__icontains=search)
           
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column,request):
        return False
class Module(BaseModel):
    class Meta:
        db_table = '"documentuploader_module"'

    
    module = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255,blank=True)
    myclass = models.ForeignKey('academics.Classes', on_delete=models.CASCADE, null=True)
    status = models.SmallIntegerField(default=1)

    objects = models.Manager() # The default manager.
    filter_objects = ModuleManager()

    columns = ['id','module','myclass.classname','description','status']
    order_columns = ['id','module','myclass.classname','description','status']
    
    

   