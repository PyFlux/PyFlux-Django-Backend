from rest_framework import serializers
from documentuploader.models.Chapter import Chapter
from documentuploader.models.Module import Module
from documentuploader.models.Fileuploader import Fileupload
from documentuploader.models.TempFileuploader import TempFileupload
from documentuploader.models.StudentFileuploader import StudentFileupload
from shared.fileserializer import Base64ImageField, Base64FileField


class FileuploadSerializer(serializers.ModelSerializer):
    
    file = Base64FileField(
      max_length=None, use_url=True, required=False, allow_empty_file=True,
    )
    class Meta:
        model = Fileupload
        fields = "__all__"
class ChapterSerializer(serializers.ModelSerializer):

    # file = Base64FileField(
    #   max_length=None, use_url=True, required=False, allow_empty_file=True,
    # )

    fileuploadfields = FileuploadSerializer(many=True, read_only=True)
    
    class Meta:
        model = Chapter
        fields = "__all__"

class ModuleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Module
        fields = "__all__"
class TempFileuploadSerializer(serializers.ModelSerializer):
    
    file = Base64FileField(
      max_length=None, use_url=True, required=False, allow_empty_file=True,
    )

    class Meta:
        model = TempFileupload
        fields = "__all__"

class StudentFileuploadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudentFileupload
        fields = "__all__"
