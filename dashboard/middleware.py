#from rest_framework.exceptions import APIException
from django.http import HttpResponse
from re import compile, sub
# from dashboard.models import AclPermissions,SubSubMenus
from rest_framework.authtoken.models import Token

from dashboard.models import SystemSettings

ANONYMOUS_USER_URLS = [
 # r'^about\.html$',
 # r'^legal/', # allow the entire /legal/* subsection
    r'^$',
    r'^static/',
    r'^api-token-auth/',
    r'^api-auth/',
    r'^admin/',
    r'^media/',
    r'^mobileapi/',
    r'^verify/', # email, mobile verification
]
EXEMPT_URLS = [compile(expr) for expr in ANONYMOUS_USER_URLS]

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)

        """
        this will activate maintenance mode
        please check 
        + frontend/src/app/shared/errorpages/maintenance.component.ts
        + frontend/src/app/shared/jwt.interceptor.ts
        """
        sysconf = SystemSettings.objects.filter(status=1,key = 'maintenance_mode')
        # maintenance = False
        if sysconf and sysconf[0].value == '1':
            if request.user.is_authenticated and request.user.user_type in ['SU','A']:
                # userttype such as SUPER ADMIN, ADMIN can work on maintanance mode
                print ('Maintenance Mode Activated')
            else:
                return HttpResponse('Service Unavailable', status=503)

        path = request.path_info.lstrip('/')
        if not request.user.is_authenticated:
            if not any(m.match(path) for m in EXEMPT_URLS):
                return HttpResponse('Unauthorized', status=401)


        return response
