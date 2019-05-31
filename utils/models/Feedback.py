from django.db import models
from django.conf import settings
from django.db.models import Q
from shared.models import BaseModel, BaseModelManager
import datetime

class FeedbackManager(BaseModelManager):   

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

    def render_column(self, row, column,request):
     
        if column == 'custom_status':
            if row.status == 1:
             return '<i class="fa fa-check"></i> Active' 
            elif row.status == 0 : 
                return '<i class="fa fa-times"></i> Inactive'
            
            elif row.status == 2 :
                return '<i class="fa fa-spinner"></i> Resolved'
            elif row.status == 3 :
                return '<i class="fa fa-spinner"></i> InProgress'
            else :
                return '<i class="fa fa-thumbs-up" aria-hidden="true"></i> Closed'

        else:
            return False
class Feedback(BaseModel):
    class Meta:
        db_table = '"utils_feedback"'

    user = models.ForeignKey('dashboard.Users', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True)
    description= models.CharField(max_length=255, null=True)
    email = models.NullBooleanField(default=False)
    status = models.SmallIntegerField(default=1)
    def __str__(self):
        return "%s" % (self.name)

    objects = models.Manager() # The default manager.
    filter_objects = FeedbackManager()

    columns = ['id','name','description','custom_status',]
    order_columns = ['id','name','description','custom_status',]
    
    

   