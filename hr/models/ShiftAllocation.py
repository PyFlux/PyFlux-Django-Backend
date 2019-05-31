from django.db import models
from shared.models import BaseModel
from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class ShiftAllocationManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'designation.emp_designation_name':
                q |= Q(designation__emp_designation_name__icontains=search)
            
            if col == 'employee_category.employee_category_name':
                q |= Q(employee_category__employee_category_name__icontains=search)
            
            if col == 'employee_name.first_name':
                q |= Q(employee_name__first_name__icontains=search)
                
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column, request):
        return False

class ShiftAllocation(BaseModel):
    class Meta:
        db_table = '"hr_emp_config_shift_allocation"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    designation =  models.ForeignKey('hr.Designation', on_delete=models.CASCADE, null=True)
    employee_category =  models.ForeignKey('hr.EmployeeCategory', on_delete=models.CASCADE, null=True)
    shift_assign =  models.ForeignKey('hr.Shift', on_delete=models.CASCADE, null=True)
    employee_name = models.ForeignKey('dashboard.Users', on_delete=models.CASCADE, null=True)
    employee_shift_new_date = models.DateField(null=True)
    employee_shift_old_date = models.DateField(null=True)
    status = models.SmallIntegerField(default=1, null=True)
    
    columns = ['id', 'designation.emp_designation_name', 'employee_category.employee_category_name', 'employee_name.full_name', 'status']
    order_columns = ['id',  'designation.emp_designation_name', 'employee_category.employee_category_name', 'employee_name.first_name', 'status', '']
    
    objects = models.Manager() # The default manager.
    filter_objects = ShiftAllocationManager()