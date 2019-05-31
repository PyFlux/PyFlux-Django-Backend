from django.db import models
from django.db.models import Q
from shared.models import BaseModel, BaseModelManager
import datetime

class TaskManager(BaseModelManager):   

    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'task_name':
                q |= Q(task_name__icontains=search)
           
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
       
        filter_taskmanagements = params['request'].data.get('filter_taskmanagements', None)
        # print(filter_taskmanagements['id'])
        if filter_taskmanagements:
            qs = qs.filter(Q(assigned_to__id = filter_taskmanagements['id']) | Q(assigned_by__id = filter_taskmanagements['id']) )
            
        # if(qs.count() == 0):

        #     print(qs.count())
        #     qs = qs.filter(assigned_by__id = filter_taskmanagements['id'])
        #     print(qs)
            
        # elif filter_taskmanagements:
        #     qs = qs.filter(assigned_by__id = filter_taskmanagements['id'])
        #     print(qs)   
        # if filter_taskmanagements:
        #     qs = qs.filter(assigned_by__first_name = filter_taskmanagements)
        


        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column,request):
     
        if column == 'custom_status':
            if row.status == 1:
             return '<i class="fa fa-check"></i> Assigned' 
            elif row.status == 0 : 
                return '<i class="fa fa-times"></i> Incomplete'
            
            elif row.status == 2 :
                return '<i class="fa fa-spinner"></i> Complete'
            

        else:
            return False
class TaskManagement(BaseModel):
    class Meta:
        db_table = '"utils_taskmanagement"'

    task_name = models.CharField(max_length=255, null=True)
    description= models.CharField(max_length=255,blank=True)
    end_date = models.DateField(null=True)
    assigned_to = models.ManyToManyField('dashboard.Users',related_name='assigned_to',blank=True)
    assigned_by = models.ManyToManyField('dashboard.Users',related_name='assigned_by',blank=True)
    status = models.SmallIntegerField(default=1)

    def __str__(self):
        return "%s" % (self.task_name)

    objects = models.Manager() # The default manager.
    filter_objects = TaskManager()

    columns = ['id','task_name','description','end_date','get_assignedto_users','get_assignedby_users','custom_status',]
    order_columns = ['id','task_name','description','end_date','assigned_to','assigned_by','custom_status',]
    
    

    @property
    def get_assignedto_users(self):
        return ", ".join([s.first_name for s in self.assigned_to.all()])

    @property
    def get_assignedby_users(self):
        return ", ".join([s.first_name for s in self.assigned_by.all()])