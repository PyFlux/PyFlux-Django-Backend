from django.db import models
from shared.models import BaseModel, BaseModelManager
# from academics.models.Classes import Classes
from django.conf import settings
from academics.models import AssignClasswiseTeacher, Classes
from django.db.models import Q


class EmployeeMasterManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'emp_user.first_name':
                q |= Q(emp_user__first_name__icontains=search)
            
            if col == 'emp_user_prof.designation':
                q |= Q(emp_user_prof__designation__emp_designation_name__icontains=search)
            
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        filter_designations = params['request'].data.get('filter_designations', None)
        filter_stafftypes = params['request'].data.get('filter_stafftype', None)
        if (filter_designations):
            qs = qs.filter(emp_user_prof__designation_id = filter_designations)
        if (filter_stafftypes):
            qs = qs.filter(emp_details__emp_staff_type = filter_stafftypes)
        qs = self.filter_search(qs,params['search'])

        return qs
    
    def render_column(self, row, column, request):
       if column == 'emp_user.first_name':
          return '''
               <a style="text-decoration:none" onMouseOver="this.style.color='#343396';style='text-decoration:underline'" onMouseOut="this.style.color=''; style='text-decoration:None'"  href="hr/employee/{id}" target="_blank">{full_name}</a>
           '''.format(id = row.id,full_name=row.emp_user.full_name)
          
       else:
           return False

class EmployeeMaster(BaseModel):
    class Meta:
        db_table = '"emp_master"'
    emp_details = models.ForeignKey('hr.Employee', on_delete=models.CASCADE, related_name='emp_details', null=True)
    emp_user = models.ForeignKey('dashboard.Users', on_delete=models.CASCADE, related_name='emp_user', null=True)
    emp_user_prof = models.ForeignKey('dashboard.UserProfile', on_delete=models.CASCADE, related_name='emp_user_prof' ,null=True)
    status = models.SmallIntegerField(default = 1)

    columns = ['id', 'emp_user.first_name', 'designation_class', 'contact_details', 'status']
    order_columns = ['id',  'emp_user.first_name', 'emp_user_prof.designation', '',  'status', '']

    objects = models.Manager() # The default manager.
    filter_objects = EmployeeMasterManager()

    @property
    def contact_details(self):            
         return "{p.temp_address} <br>{p.personal_mobile_no} <br>{email}".format(p = self.emp_user_prof, email = self.emp_user.email)
    
    @property
    def designation_class(self):
        if(self.emp_details.emp_staff_type=='T'):
            teacher_classes = []
            for academic_classes in self.emp_details.user.assignclasswiseteacher_set.filter(status=1,deleted_at=None):
                teacher_classes.append(academic_classes.available_class.classname)
            if (teacher_classes):
                return "%s - %s" % (self.emp_user_prof.designation.emp_designation_name, ','.join(teacher_classes))
            else:
                return "%s" % (self.emp_user_prof.designation.emp_designation_name)
        else:
            return "%s" % (self.emp_user_prof.designation.emp_designation_name)
