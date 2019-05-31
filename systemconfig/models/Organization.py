from django.db import models
from shared.models import BaseModel

from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class OrganizationManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'org_name':
                q |= Q(org_name__icontains=search)
            
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column, request):
        return False

class Organization(BaseModel):
    class Meta:
        db_table = '"system_config_organization"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    org_name = models.CharField(max_length=255, null=True)
    org_alias = models.CharField(max_length=255,blank=True, null=True)
    org_code = models.CharField(max_length=255,blank=True, null=True)
    org_address_line1 = models.CharField(max_length=255, null=True)
    org_address_line2 = models.CharField(max_length=255, null=True)
    org_phone = models.CharField(max_length=255, null=True)
    org_email = models.CharField(max_length=255, null=True)
    org_website = models.CharField(max_length=255, null=True,blank=True)
    org_logo = models.FileField(upload_to='organization/')
    org_stu_prefix = models.CharField(max_length=255, null=True)
    org_emp_prefix = models.CharField(max_length=255, null=True)
    institute_info = models.TextField(null=True)
    institute_image = models.ImageField(upload_to='organization/')
    status = models.SmallIntegerField(default=1)

    columns = ['id','org_name', 'org_alias', 'org_phone', 'org_email', 'org_website', 'status']
    order_columns = ['id','org_name', 'org_alias', 'org_phone', 'org_email', 'org_website','status','']
    
    
    objects = models.Manager() # The default manager.
    filter_objects = OrganizationManager()

    def __str__(self):
        return "%s" % (self.org_name)