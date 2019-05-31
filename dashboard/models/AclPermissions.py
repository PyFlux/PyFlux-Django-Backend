from shared.models import BaseModel
from django.db import models
# from . import Roles

class AclPermissions(BaseModel):
    """
    What a the permissions for a role
    """
    role = models.ForeignKey('Roles', on_delete= models.CASCADE)
    menu_text = models.CharField(max_length=128)
    link = models.CharField(max_length=128,blank=True)    
    icon = models.CharField(max_length=128, blank=True) # Fontawesome Icon
    acl_key = models.CharField(max_length=128, blank=True)
    parent_menu = models.CharField(max_length=128, blank=True)
    level = models.CharField(max_length=128, blank=True)
    ordering = models.IntegerField(default=0) #CharField(max_length=128, blank=True)    
    view = models.BooleanField(default=False)    
    approval_level_1 = models.CharField(max_length=128, blank=True)
    approval_level_2 = models.CharField(max_length=128, blank=True)

    app_name = models.CharField(max_length=128, blank=True)
    model_name = models.CharField(max_length=128, blank=True)

    def viewable_submenus(self):
        # https://stackoverflow.com/a/48429368/2351696
        return SubMenus.objects.filter(main_menu=self, view = True).order_by('-ordering')

class SubMenus(BaseModel):
    main_menu = models.ForeignKey('AclPermissions', related_name='submenus',on_delete= models.CASCADE, null = True)
    menu_text = models.CharField(max_length=128)
    acl_key = models.CharField(max_length=128, blank=True)
    link = models.CharField(max_length=128, blank=True)
    view = models.BooleanField(default=False)
    ordering = models.IntegerField(default=0) #CharField(max_length=128, blank=True) 
       
    def viewable_subsubmenus(self):
        return SubSubMenus.objects.filter(sub_menu=self, view = True).order_by('-ordering')

class SubSubMenus(BaseModel):
    sub_menu = models.ForeignKey('SubMenus', related_name='subsubmenus',on_delete= models.CASCADE, null = True)
    menu_text = models.CharField(max_length=128)
    acl_key = models.CharField(max_length=128, blank=True)
    link = models.CharField(max_length=128)
    view = models.BooleanField(default=False)
    add = models.BooleanField(default=False)
    edit = models.BooleanField(default=False)
    trash = models.BooleanField(default=False)
    ordering = models.IntegerField(default=0) #CharField(max_length=128, blank=True)