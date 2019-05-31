from rest_framework.response import Response
from rest_framework.views import APIView
from documentuploader.models import Chapter,Module,Fileupload,StudentFileupload
from documentuploader.serializers import FileuploadSerializer
from shared.views import TimeDelayed_APIView
from json import loads, dumps
from academics.models import AssignClasswiseTeacher
from dashboard.models import Users
class getDocuments(TimeDelayed_APIView):

    def getClassTeacher(self,class_id):

        
        teacher_data = AssignClasswiseTeacher.objects.filter(available_class = class_id)
    
        
        for teacher in teacher_data:
            teacher_name = Users.objects.filter(id = teacher.teacher_id)
            for teacher in teacher_name:
                teachername = teacher.full_name
       
        
        return teachername
   
    def get(self, request, format=None):

      
        student_files = StudentFileupload.objects.filter(student_id = request.user.id)
      
        result = []
        # files = Fileupload.objects.filter(student_id = request.user.id)
        for file in student_files:
            serializer = FileuploadSerializer(Fileupload.objects.filter(id = file.documents_id,deleted_at = None),many=True, context={'request': request})
            
            documents = loads(dumps(serializer.data))
            for document in documents:
              
                chapter_id = document['chapter_id']
                module_id =Chapter.objects.filter(id = chapter_id).values()
                for module in module_id:
                    module = Module.objects.filter(id = module['module_id']).values()
                
                    for mod in module:
                        module_name = mod['module']
                        class_id = mod['myclass_id']
                        teacher = self.getClassTeacher(class_id)
                       

                queryset3 =  dict(file = document['file'],
                    filename = document['filename'],
                    module_name = module_name,
                    teacher = teacher
                    )
                    
                result.append(queryset3)
       
            

        return Response(result)