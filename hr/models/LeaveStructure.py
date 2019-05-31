from django.db import models
from shared.models import BaseModel
from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class LeaveStructureManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'leave_structure':
                q |= Q(leave_structure__icontains=search)
            
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column, request):
        return False

class LeaveStructure(BaseModel):
    class Meta:
        db_table = '"hr_leave_structure"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    leave_structure = models.CharField(max_length=255, null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    status = models.SmallIntegerField(default=1, null=True)
    
    columns = ['id', 'leave_structure', 'start_date', 'end_date', 'status']
    order_columns = ['id',  'leave_structure', 'start_date', 'end_date', 'status', '']

    objects = models.Manager() # The default manager.
    filter_objects = LeaveStructureManager()