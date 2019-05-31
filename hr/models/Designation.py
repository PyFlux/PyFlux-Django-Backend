from django.db import models
from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class DesignationManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'emp_designation_name':
                q |= Q(emp_designation_name__icontains=search)
            
            if col == 'emp_designation_alias':
                q |= Q(emp_designation_alias__icontains=search)
            
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column, request):
        return False

class Designation(BaseModel):
    class Meta:
        db_table = '"hr_emp_designation"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    emp_designation_name = models.CharField(max_length=255, blank=True, null=True)
    emp_designation_alias = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField(default=1, null=True)

    columns = ['id', 'emp_designation_name', 'emp_designation_alias', 'status']
    order_columns = ['id',  'emp_designation_name', 'emp_designation_alias', 'status', ''] 

    objects = models.Manager() # The default manager.
    filter_objects = DesignationManager()

    def __str__(self):
        return "%s" % (self.emp_designation_name)