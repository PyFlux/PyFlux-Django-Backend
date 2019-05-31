from django.db import models
from django.conf import settings
 
from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class EmailCredentialsManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'smtp_user_name':
                q |= Q(smtp_user_name__icontains=search)
            
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column, request):
        return False
        
security_choices = (('None','None'),('STARTTLS','STARTTLS'),)
port_choices = (('587','587'),)

class EmailCredentials(BaseModel):
    class Meta:
        db_table = '"system_config_email_credentials"'
    smtp_user_name = models.CharField(max_length=255, null=True)
    smtp_password = models.CharField(max_length=255, null=True)
    smtp_hostname = models.CharField(max_length=255, null=True)
    smtp_port = models.CharField(max_length=255, choices=port_choices, null=True)
    smtp_security = models.CharField(max_length=255, choices=security_choices, null=True)
    smtp_auth_method = models.CharField(max_length=255, null=True)
    status = models.SmallIntegerField()
     
    columns = ['id','smtp_user_name','status']
    order_columns = ['id','smtp_user_name','status','']

    objects = models.Manager() # The default manager.
    filter_objects = EmailCredentialsManager()