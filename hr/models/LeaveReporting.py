from django.db import models
from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class LeaveReportingManager(BaseModelManager):
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

class LeaveReporting(BaseModel):
    class Meta:
        db_table = '"hr_leave_reporting"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    report_from = models.ForeignKey('dashboard.Roles', on_delete=models.CASCADE, related_name='leave_reporting', null=True)
    report_to = models.ManyToManyField('dashboard.Roles',blank=True)
   
    status = models.SmallIntegerField(default=1, null=True)

    columns = ['id', 'report_from.name', 'get_to_users', 'status']
    order_columns = ['id',  'report_from', 'report_to', 'status']

    objects = models.Manager() # The default manager.
    filter_objects = LeaveReportingManager()


    @property
    def get_to_users(self):
        return ", ".join([s.name for s in self.report_to.all()])

   
    