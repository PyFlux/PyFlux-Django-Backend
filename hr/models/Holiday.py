from django.db import models
from shared.models import BaseModel
import datetime
from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class HolidayManager(BaseModelManager):
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
        return False

class Holiday(BaseModel):
    class Meta:
        db_table = '"hr_emp_config_holiday"'
    # Existing fields
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    name = models.CharField(max_length=255, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=255, null=True)
    status = models.SmallIntegerField(default=1, null=True)
    
    columns = ['id', 'name', 'start_date_format', 'end_date_format', 'status']
    order_columns = ['id',  'name', 'start_date', 'end_date', 'status', '']
    
    objects = models.Manager() # The default manager.
    filter_objects = HolidayManager()

    @property
    def start_date_format(self):
        if(self.start_date):
            d = datetime.datetime.strptime(str(self.start_date), '%Y-%m-%d')
            format_date = datetime.date.strftime(d, "%d/%m/%Y")
            return "%s" % ( format_date )



    @property
    def end_date_format(self):
        if(self.end_date):
            d = datetime.datetime.strptime(str(self.end_date), '%Y-%m-%d')
            format_date = datetime.date.strftime(d, "%d/%m/%Y")
            return "%s" % ( format_date )

    def __str__(self):
        return "%s" % (self.name)