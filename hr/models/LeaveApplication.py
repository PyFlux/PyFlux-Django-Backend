from django.db import models
from shared.models import BaseModel, BaseModelManager
from django.db.models import Q
import datetime
from datetime import date
class LeaveApplicationManager(BaseModelManager):
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

    def render_column(self, row, column, request):
        if column == 'application_status':
            if row.status == str(1):
                return '<i class="fa fa-check"></i> Active'
            elif row.status == str(0):
                return'<i class="fa fa-times"></i> Inactive'
            elif row.status == str(2):
                return'<i class="fa fa-file" style="color:darkblue;"></i> Applied'
            elif row.status == str(3):
                return'<i class="fa fa-thumbs-up" style="color:green;"></i> Approved'
            elif row.status == str(4):
                return'<i class="fa fa-thumbs-down" style="color:red;"></i> Rejected'
        else:
            return False

unit_choices = (
     ('1', 'Full Day'),
     ('0','Half Day'),
)

shift_choices = (
     ('1', 'Morning'),
     ('0','AfterNoon'),
)

status_choices = (
     ('4','Rejected'),
     ('3','Approved'),
     ('2','Applied'),
     ('1','Publish'),
     ('0','Unpublish'),
)

class LeaveApplication(BaseModel):
    class Meta:
        db_table = '"hr_leave_application"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    user = models.ForeignKey('dashboard.Users', on_delete=models.CASCADE, null=True)
    units = models.CharField(max_length=10, choices=unit_choices, null=True)
    leave_type = models.ForeignKey('hr.LeaveType', on_delete=models.CASCADE, null=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)
    shift = models.CharField(max_length=255, null=True, choices=shift_choices)
    reason = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=10, choices=status_choices, null=True)

    columns = ['id', 'user.full_name', 'leave_type.leave_name', 'leave_time',  'application_status']
    order_columns = ['id', 'user', 'leave_type.leave_name','leave_time', 'application_status']

    objects = models.Manager() # The default manager.
    filter_objects = LeaveApplicationManager()


    @property
    def leave_time(self):
        if self.units == '0':
            d = datetime.datetime.strptime(str(self.from_date), '%Y-%m-%d')
            format_date = datetime.date.strftime(d, "%d/%m/%Y")
            return "%s, %s-%s" % (format_date, self.get_units_display(),  self.get_shift_display() )
        else:
            d = datetime.datetime.strptime(str(self.from_date), '%Y-%m-%d')
            format_date = datetime.date.strftime(d, "%d/%m/%Y")
            t = datetime.datetime.strptime(str(self.to_date), '%Y-%m-%d')
            format_to_date = datetime.date.strftime(t, "%d/%m/%Y")
            delta = (self.to_date - self.from_date)
            return "%s to %s (%s day)" % (format_date, format_to_date, delta.days+1)
