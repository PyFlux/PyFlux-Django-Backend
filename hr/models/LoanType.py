from django.db import models
from shared.models import BaseModel
from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class LoanTypeManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'loan_name':
                q |= Q(loan_name__icontains=search)
            
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column, request):
        return False

class LoanType(BaseModel):
    class Meta:
        db_table = '"hr_emp_config_loan_type"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    loan_name = models.CharField(max_length=255, null=True)
    loan_details = models.CharField(max_length=500, null=True)
    status = models.SmallIntegerField(default=1, null=True)
    
    columns = ['id', 'loan_name', 'loan_details', 'status']
    order_columns = ['id',  'loan_name', 'loan_details', 'status', '']

    objects = models.Manager() # The default manager.
    filter_objects = LoanTypeManager()