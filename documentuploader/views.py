from django.db.models import Max
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from django.conf import settings

from documentuploader.models.Module import Module

from documentuploader.models.Chapter import Chapter
from documentuploader.models.Fileuploader import Fileupload
from documentuploader.models.TempFileuploader import TempFileupload
from documentuploader.models.StudentFileuploader import StudentFileupload

# Create your views here.
from documentuploader.serializers import ChapterSerializer,ModuleSerializer,\
FileuploadSerializer,TempFileuploadSerializer,StudentFileuploadSerializer

from shared.views import CURDViewSet
from dashboard.models import *
from django.db.models import Q
# from django.template import loader, Context
import documentuploader
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
import os
import shutil
from datetime import datetime
from academics.models import *
from students.models import *



class FileuploadListAPIView(CURDViewSet):
    queryset = Fileupload.objects.filter(status=1, deleted_at=None)
    serializer_class = FileuploadSerializer

class TempFileuploadListAPIView(CURDViewSet):
    queryset = TempFileupload.objects.filter(status=1, deleted_at=None)
    serializer_class = TempFileuploadSerializer
    
class StudentFileuploadListAPIView(CURDViewSet):
    queryset = StudentFileupload.objects.filter(status=1, deleted_at=None)
    serializer_class = StudentFileuploadSerializer
      
class ChapterListAPIView(CURDViewSet):
    
    queryset = Chapter.objects.filter(status=1, deleted_at=None)
    serializer_class = ChapterSerializer

    def getClassStudents(self,class_id):

        student_data = Student.objects.filter(myclass_id = class_id)
        result = []
        for student in student_data:
            result.append(student.user_id)
        
        data = {'students':result}
        
        return result
    def create(self, request, *args, **kwargs):

        module = request.data['module']
        chapter = Chapter.objects.create(
            chapter = request.data['chapter'],
            description = request.data['description'],
            module_id = module
            )

        fileuploads = TempFileupload.objects.filter(token = request.data['token'])
        
        module_class = Module.objects.filter(id = module)
        for clas in module_class:
            class_id = clas.myclass_id
            
        for fileupload in fileuploads:
            obj = Fileupload(deleted_at = None)
            obj.chapter_id = chapter
            obj.order = fileupload.order
            obj.file = fileupload.file.name
            obj.filename = fileupload.filename
            obj.save()
            
            students = self.getClassStudents(class_id)
            result = []
            for stu in students:
            
                StudentFileupload.objects.create(
                    chapter = chapter,
                    documents_id = obj.id,
                    student_id = stu,
                    status = fileupload.status
                    
                    )

        TempFileupload.objects.filter(token = request.data['token']).update(
            deleted_at = datetime.datetime.now()
            )

        return Response('test')

    def update(self, request, *args, **kwargs):

        
        module = request.data['module']
        subject = Module.objects.get(id = module )
        chapter = Chapter.objects.filter(pk = request.data['id']).update(

            chapter = request.data['chapter'],
            description = request.data['description'],
            module_id = module
            )
        queryset = Fileupload.objects.filter(chapter_id_id = request.data['id']).delete()
        module_class = Module.objects.filter(id = module)
        for clas in module_class:
            class_id = clas.myclass_id
        fileuploads = TempFileupload.objects.filter(token = request.data['token'])
        

        dcment = []
        for fileupload in fileuploads: 
            documents =  Fileupload.objects.create(
                chapter_id_id = request.data['id'],
                order = fileupload.order,
                file = fileupload.file.name,
                filename = fileupload.filename
                )
            dcment.append(documents)
           
        students = self.getClassStudents(class_id)
        queryset2 = StudentFileupload.objects.filter(chapter_id = request.data['id']).delete()
        result = []
        for stu in students:
          for doc in dcment:
            StudentFileupload.objects.create(
                chapter_id = request.data['id'],
                documents_id = doc.id,
                student_id = stu,
                status = doc.status
                )

            TempFileupload.objects.filter(token = request.data['token']).update(
            deleted_at = datetime.datetime.now()
            )
        return Response('test') 



class ModuleListAPIView(CURDViewSet):
    queryset = Module.objects.filter(status=1, deleted_at=None)
    serializer_class = ModuleSerializer














