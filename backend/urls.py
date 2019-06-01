"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
#from rest_framework.authtoken.views import obtain_auth_token
from shared.views import CustomAuthToken, DatatableListJson #datatable_json

from dashboard.urls import router as dashboard_router
from systemconfig.urls import router as systemconfig_router
from utils.urls import router as utils_router

router = routers.DefaultRouter()
router.registry.extend(dashboard_router.registry)
router.registry.extend(systemconfig_router.registry)

router.registry.extend(utils_router.registry)

# https://stackoverflow.com/questions/52898142
# from django.views.static import serve
# from django.contrib.auth.decorators import login_required

# # @login_required
# def serve_protected_media(request, path, document_root=None, show_indexes=False):
#     token_key = request.META
#     print(token_key, request.user)
#     # token = Token.objects.get(key=token_key)
#     # request.user = token.user
#     return serve(request, path, document_root, show_indexes)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datatable_json/', DatatableListJson.as_view()),#datatable_json, name='datatableView'),
    path('', include(router.urls)),
    path('dashboard/', include('dashboard.urls')),
    path('systemconfig/', include('systemconfig.urls')),
    path('usermanagement/', include('usermanagement.urls')),
    path('utils/', include('utils.urls')),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
