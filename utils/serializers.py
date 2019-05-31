from rest_framework import serializers
from .models import TaskManagement,Feedback,Category,SubCategory
# from .models import Feedback
from utils.models.Template import Template
from utils.models.Category import Category
from utils.models.Subcategory import SubCategory
# from shared.fileserializer import Base64ImageField
class TaskManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskManagement
        fields = "__all__"

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"

class TemplateSerializer(serializers.ModelSerializer):
    # template = Base64ImageField(
    #    max_length=None, use_url=True, required=False
    # )
    class Meta:
        model = Template
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"

class SubCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SubCategory
        fields = "__all__"