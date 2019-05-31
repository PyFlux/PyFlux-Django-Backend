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

from academics.urls import router as academics_router
from administration.urls import router as administration_router
from communications.urls import router as communications_router
from dashboard.urls import router as dashboard_router
from fees.urls import router as fees_router
from hr.urls import router as hr_router
from library.urls import router as library_router
from parents.urls import router as parents_router
from students.urls import router as students_router
from systemconfig.urls import router as systemconfig_router
from exammanagement.urls import router as exammanagement_router
from events.urls import router as events_router
from admissions.urls import router as admissions_router
from mobileapi.urls import router as mobileapi_router
from extracurricularactivities.urls import router as extracurricularactivities_router
# from taskmanagement.urls import router as taskmanagement_router
# from feedback.urls import router as feedback_router

from documentuploader.urls import router as documentuploader_router
from utils.urls import router as utils_router
from hostel.urls import router as hostel_router
from inventory.urls import router as inventory_router

router = routers.DefaultRouter()
router.registry.extend(academics_router.registry)
router.registry.extend(administration_router.registry)
router.registry.extend(communications_router.registry)
router.registry.extend(dashboard_router.registry)
router.registry.extend(fees_router.registry)
router.registry.extend(hr_router.registry)
router.registry.extend(library_router.registry)
router.registry.extend(parents_router.registry)
router.registry.extend(students_router.registry)
router.registry.extend(systemconfig_router.registry)
router.registry.extend(exammanagement_router.registry)
router.registry.extend(admissions_router.registry)
router.registry.extend(events_router.registry)
router.registry.extend(mobileapi_router.registry)
router.registry.extend(extracurricularactivities_router.registry)
# router.registry.extend(taskmanagement_router.registry)
# router.registry.extend(feedback_router.registry)

router.registry.extend(documentuploader_router.registry)
router.registry.extend(utils_router.registry)
router.registry.extend(hostel_router.registry)
router.registry.extend(inventory_router.registry)
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
    
    path('academics/', include('academics.urls')),
    path('admissions/', include('admissions.urls')),
    path('administration/', include('administration.urls')),
    
    path('communications/', include('communications.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('fees/', include('fees.urls')),
    path('hr/', include('hr.urls')),
    path('library/', include('library.urls')),
    path('parent/', include('parents.urls')),
    path('students/', include('students.urls')),
    path('systemconfig/', include('systemconfig.urls')),
    path('exammanagement/', include('exammanagement.urls')),
    path('events/', include('events.urls')),
    path('mobileapi/', include('mobileapi.urls')),
    path('extracurricularactivities/', include('extracurricularactivities.urls')),
    path('usermanagement/', include('usermanagement.urls')),
    path('reports/', include('reports.urls')),
    path('timetable/', include('timetable.urls')),
    # path('taskmanagement/', include('taskmanagement.urls')),
    # path('feedback/', include('feedback.urls')),

    # path('templatemanagement/', include('template.urls')),
    path('documentuploader/', include('documentuploader.urls')),
    path('notifications/', include('notifications.urls')),
    path('utils/', include('utils.urls')),
    path('hostel/', include('hostel.urls')),
    path('inventory/', include('inventory.urls')),
    # path('verify/', include('verify.urls')),

    
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
