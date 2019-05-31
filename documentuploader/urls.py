from django.urls import path, include
from rest_framework import routers
from documentuploader.views import (ChapterListAPIView,
	ModuleListAPIView,FileuploadListAPIView,TempFileuploadListAPIView,StudentFileuploadListAPIView)

router = routers.DefaultRouter()


router.register(r'chapter', ChapterListAPIView)
router.register(r'module', ModuleListAPIView)
router.register(r'fileupload', FileuploadListAPIView)
router.register(r'tempfileupload', TempFileuploadListAPIView)
router.register(r'studentfileupload', StudentFileuploadListAPIView)


urlpatterns = [
    path('', include(router.urls)),
   
   
]
    