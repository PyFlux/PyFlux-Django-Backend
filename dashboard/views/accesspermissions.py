"""
* Get sidebar menus
* Save Acl Permissions
* To get SubSubmenu details for create add/edit/delete toolbar.
"""
from rest_framework.response import Response
from rest_framework import authentication
from shared.views import TimeDelayed_APIView

from dashboard.serializers import create_aclpermissions_for_role, AclPermissionsSerializer, \
    SideBarMenusSerializer, SubSubMenusSerializer
from dashboard.models import AclPermissions, Roles, SubMenus, SubSubMenus, UserRoles

class DashboardMenu(TimeDelayed_APIView):
    """
    To get all side bar menus.

    * Requires token authentication.    
    """
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        role = request.GET.get('roleid', '')
        # print('role',role)
        if role == 'for_sidebar_menu':
            "For sidebar menu"
            try:
                userrole = UserRoles.objects.get(user=request.user)
                role = userrole.role
            except UserRoles.DoesNotExist:
                # if user doesn't have any userroles
                role, created = Roles.objects.get_or_create(name='Anonymous')
                if created: create_aclpermissions_for_role(role)

            queryset = AclPermissions.objects.filter(role_id=role, view=True).order_by('-ordering', 'menu_text')
            serializer = SideBarMenusSerializer(queryset, many=True)
        else:
            "Get aclpermission menus, submenus and subsubmenus for display of Aclpermision edit form"
            queryset = AclPermissions.objects.filter(role_id=role).order_by('menu_text')
            serializer = AclPermissionsSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Save aclpermission checkbox datas
        """
        chk_value = request.data['check_box']
        chk_type = request.data['chk_type']
        # view_all,add_all, edit_all, row_all
        if chk_type in ['view_all', 'all', 'add_all', 'edit_all']:
            # if all checkbox is clicked
            role_id = request.data['role']
            items = AclPermissions.objects.filter(role_id=role_id)
            if chk_type in ['view_all', 'all']:
                items.update(view=chk_value)

            for menu in items:
                # if chk_type in ['view_all','all']:
                # menu.submenus.all().update(view = chk_value)
                for submenu in menu.submenus.all():
                    if chk_type == 'all':
                        submenu.view = chk_value
                        submenu.save()
                        submenu.subsubmenus.all().update(
                            view=chk_value,
                            add=chk_value,
                            edit=chk_value,
                            trash=chk_value)
                    elif chk_type == 'view_all':
                        submenu.view = chk_value
                        submenu.save()
                        submenu.subsubmenus.all().update(view=chk_value, )
                    elif chk_type == 'add_all':
                        submenu.subsubmenus.all().update(add=chk_value, )
                    elif chk_type == 'edit_all':
                        submenu.subsubmenus.all().update(edit=chk_value, )
                    elif chk_type == 'delete_all':
                        submenu.subsubmenus.all().update(trash=chk_value, )

        elif 'submenus' in request.data:
            # if main menu checkbox clicked
            chk_id = request.data['id']
            item = AclPermissions.objects.get(id=chk_id)
            if chk_type == 'ordering':
                item.ordering = chk_value
            else:
                item.view = chk_value
            item.save()

        elif 'subsubmenus' in request.data:
            # if submenu checkbox is clicked
            chk_id = request.data['id']
            item = SubMenus.objects.get(id=chk_id)
            if chk_type == 'ordering':
                item.ordering = chk_value
            else:
                item.view = chk_value
            item.save()

        elif 'sub_menu' in request.data:
            # if subsubmenu checkbox is clicked
            chk_id = request.data['id']
            item = SubSubMenus.objects.get(id=chk_id)
            if chk_type == 'ordering':
                item.ordering = chk_value
            elif chk_type == 'add':
                item.add = chk_value
            elif chk_type == 'edit':
                item.edit = chk_value
            elif chk_type == 'delete':
                item.trash = chk_value
            elif chk_type == 'view':
                item.view = chk_value
            elif chk_type == 'row_change':
                f = chk_value
                item.view, item.add, item.edit, item.trash = (f, f, f, f)
            item.save()

        return Response('SAVED')


class getSubSubmenuDetails(TimeDelayed_APIView):
    """
    To get SubSubmenu details for create add/edit/delete toolbar.
    """
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        # print(request.data)
        menu_id = request.GET.get('id', '')
        if not menu_id: return Response('')
        queryset = SubSubMenus.objects.get(id=menu_id)
        serializer = SubSubMenusSerializer(queryset)
        return Response(serializer.data)