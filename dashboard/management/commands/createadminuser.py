from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from dashboard.models import Roles, UserRoles, AclPermissions
from dashboard.serializers import create_aclpermissions_for_role

class Command(BaseCommand):
    help = 'Creates Admin and SuperAdmin'

    def create_role(self, name, user):
        role, created = Roles.objects.get_or_create(name=name)

        UserRoles.objects.create(user=user,role = role)
        if created: create_aclpermissions_for_role(role)
        menu = AclPermissions.objects.get(role = role, menu_text= 'Control Panel')
        menu.view = True
        menu.save()
        for submenu in menu.submenus.all():
            submenu.view = True
            submenu.save()
            submenu.subsubmenus.all().update(view = True, add = True, edit =True, trash = True)

    def create_user(self,cred):
        User = get_user_model()
        if User.objects.filter(username = cred['username']):
            self.stdout.write('User with username %s already exist' %cred['username'])
            return

        user = User.objects.create_superuser(cred['username'], cred['email'],cred['password'])
        if cred['username'] == 'superadmin':
            fname,utype = 'Super Admin','SU'
        if cred['username'] == 'admin':
            fname,utype = 'Admin','A'
            
        user.first_name = fname
        user.user_type=utype
        user.save()
        self.create_role(fname,user)
        self.stdout.write(self.style.SUCCESS(
            '{0} Created Successfully.  Username: {1}, Password: {2}'.format(fname,cred['username'],cred['password'])
        ))

    def handle(self, *args, **options):
        # Create Super Admin
        users = [
            {'username':'superadmin', 'email':'superadmin@vidhyadhan.in', 'password':'superadmin123#'},
            {'username':'admin', 'email':'admin@vidhyadhan.in', 'password':'admin123#'},
        ]
        for user in users:
            self.create_user(user)