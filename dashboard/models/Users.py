from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import Q
#django.contrib.auth.models.UserManager()

from shared.models import BaseModel, BaseModelManager

class CustomUsersManager(BaseModelManager):
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
        qs = qs.filter(deleted_at__isnull=True, status =1)
        qs = self.filter_search(qs,params['search'])
        return qs

class Users(AbstractUser,BaseModel):
    # Added fields
    USER_TYPE_CHOICES = (
        ('SU', 'Super User'),
        ('A', 'Admin'),
        ('PR','Principal'),
        ('T', 'Teacher'),
        ('E', 'Employee'),
        ('S', 'Student'),
        ('P', 'Parent'),
        ('MN','Manager'),
        ('AN', 'Anonymous'),
    )
    #role = models.ForeignKey("dashboard.Roles", on_delete= models.CASCADE, blank=True, null=True)
    user_type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField(default = 1)
    
    columns = ['id','first_name','username','email','status']
    order_columns = ['','first_name','username','email','']

    objects = UserManager() 
    filter_objects = CustomUsersManager()
    
    class Meta(object):
       
        unique_together = ('email',)
   
    @property
    def full_name(self): 
        return "%s %s" % ( self.first_name.capitalize() , self.last_name.capitalize())


    @property
    def is_verified_email(self):
        if hasattr(self, 'userprofile'):
            return self.userprofile.is_verified_email
        else:
            return False 

    def __str__(self):
        return "%s" % (self.full_name)
    
   