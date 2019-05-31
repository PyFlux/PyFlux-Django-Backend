from rest_framework import serializers
from .models import (AclPermissions,SubMenus,SubSubMenus, 
    Roles,UserProfile,UserRoles, Users, UserAddress, ConfigDetail, ConfigHead)
from django.contrib.auth import get_user_model
from dashboard.image_upload import *
from shared.fileserializer import Base64ImageField

def create_aclpermissions_for_role(role):
    from dashboard.dashboard_menu import SIDE_BAR_MENUS
    for menu in SIDE_BAR_MENUS:
        model_menu = AclPermissions.objects.create(
            role = role, link = '#',menu_text= menu['menu_text'],icon = menu['menu_icon'],
        )
        for submenu in menu['sub_menu']:
            model_submenu = SubMenus.objects.create(main_menu = model_menu,menu_text = submenu['menu_text'])

            for subsubmenu in submenu['sub_sub_menu']:
                model_subsubmenu = SubSubMenus.objects.create(
                    sub_menu = model_submenu,menu_text = subsubmenu['menu_text'],link = subsubmenu['link'],
                )

class ConfigDetailSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ConfigDetail
        fields = "__all__"

class ConfigHeadSerializer(serializers.ModelSerializer):    
    class Meta:
        model = ConfigHead
        fields = "__all__"

class SubSubMenusSerializer(serializers.ModelSerializer):    
    class Meta:
        model = SubSubMenus
        fields = "__all__"

class SubMenusSerializer(serializers.ModelSerializer):
    subsubmenus = SubSubMenusSerializer(many=True, read_only=True)
    class Meta:
        model = SubMenus
        fields = ['id','menu_text','view','subsubmenus','ordering']
        
class AclPermissionsSerializer(serializers.ModelSerializer):
    submenus = SubMenusSerializer(many=True, read_only=True)
    class Meta:
        model = AclPermissions
        fields = ['id','menu_text','link','icon','view','submenus','acl_key','ordering']


# for sidebar menu initialization
class SideBarSubMenusSerializer(serializers.ModelSerializer):
    subsubmenus = SubSubMenusSerializer(many=True, read_only=True,source="viewable_subsubmenus")
    
    class Meta:
        model = SubMenus
        fields = ['id','menu_text','view','subsubmenus']


class SideBarMenusSerializer(serializers.ModelSerializer):
    submenus = SideBarSubMenusSerializer(many=True, read_only=True,source="viewable_submenus")
    class Meta:
        model = AclPermissions
        fields = ['id','menu_text','link','icon','view','submenus','acl_key']


class RolesSerializer(serializers.ModelSerializer):
    def create(self, *args, **kwargs):
        role = super().create(*args, **kwargs)        
        """
        Create Acl Permission menus with view=False
        """
        create_aclpermissions_for_role(role)
        return role
        
    class Meta:
        model = Roles
        fields = "__all__"  


class AddressSerializer(serializers.ModelSerializer):
    city_name =  serializers.ReadOnlyField(source='city.city_name')
    district_name =  serializers.ReadOnlyField(source='district.name')
    state_name =  serializers.ReadOnlyField(source='state.state_name')

    class Meta:
        model = UserAddress
        fields = "__all__"   
   
class UserProfilesSerializer(serializers.ModelSerializer):
    media = Base64ImageField(
       max_length=None, use_url=True, required=False
    )
    designation_name = serializers.ReadOnlyField(source='designation.emp_designation_name')
    religion_name = serializers.ReadOnlyField(source='religion.religion_name')
    addresses = AddressSerializer(many=True, read_only=True)
    # tmp_city =  serializers.ReadOnlyField(source='temp_city.city_name')
    # tmp_district =  serializers.ReadOnlyField(source='temp_district.name')
    # tmp_state =  serializers.ReadOnlyField(source='temp_state.state_name')
    # permt_city =  serializers.ReadOnlyField(source='permanent_city.city_name')
    # permt_district =  serializers.ReadOnlyField(source='permanent_district.name')
    # permt_state =  serializers.ReadOnlyField(source='permanent_state.state_name')
   
    class Meta:
        model = UserProfile
        fields = "__all__"   


class UserRolesSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    religion_name = serializers.ReadOnlyField(source='role.name')
    
    class Meta:
        model = UserRoles
        fields = "__all__" 

class UsersSerializer(serializers.ModelSerializer):
    # https://stackoverflow.com/a/34428116/2351696    
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super().__init__(*args, **kwargs)

    class Meta:
        model = get_user_model()
        fields = "__all__"
        # so the password field will not visible in get requests
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)

    