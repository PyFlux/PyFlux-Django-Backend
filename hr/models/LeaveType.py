from django.db import models
from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class LeaveTypeManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'leave_name':
                q |= Q(leave_name__icontains=search)
            
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column, request):
        return False

class LeaveType(BaseModel):
    class Meta:
        db_table = '"hr_leave_type"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    leave_name = models.CharField(max_length=255, null=True)
    leave_details = models.CharField(max_length=255, null=True)
    percentage_cf = models.CharField(max_length=255, null=True)
    maximum_cf = models.CharField(max_length=255, null=True)
    cf_leave_availability = models.CharField(max_length=255, null=True)
    carry_frwd = models.CharField(max_length=255, null=True)
    proportion_leave = models.CharField(max_length=255, null=True)
    status = models.SmallIntegerField(default=1, null=True)

    columns = ['id', 'leave_name', 'cf_leave_availability', 'status']
    order_columns = ['id',  'leave_name', 'cf_leave_availability', 'status', '']

    objects = models.Manager() # The default manager.
    filter_objects = LeaveTypeManager()