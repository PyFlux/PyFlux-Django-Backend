from django.db import models
from django.db.models import Q

from shared.models import BaseModel, BaseModelManager

class UserRolesManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'status']: continue

            # apply global search to all searchable columns
            q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)

    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

class UserRoles(BaseModel):
	# what about change user to onetoonefield?
    user = models.OneToOneField('Users', on_delete= models.CASCADE)
    role = models.ForeignKey('Roles', on_delete= models.CASCADE)
    status = models.SmallIntegerField(default = 1)

    columns = ['id','user.first_name','user.username','role.name','status']
    order_columns = ['','user.first_name','user.username','role.name','']

    objects = models.Manager() # The default manager.
    filter_objects = UserRolesManager()
    