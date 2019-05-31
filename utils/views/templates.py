from django.db.models import Max
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from django.conf import settings
from utils.models.Template import Template
from utils.models.Category import Category
from utils.models.Subcategory import SubCategory
# Create your views here.
from utils.serializers import TemplateSerializer,CategorySerializer,SubCategorySerializer
from shared.views import CURDViewSet
from dashboard.models import *
from django.db.models import Q
# from django.template import loader, Context
# from utils.models import template
from django import template

class TemplateListAPIView(CURDViewSet):
    queryset = Template.objects.filter(status=1, deleted_at=None)
    serializer_class = TemplateSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        t = template.Template(instance.template)
        # t = loader.get_template(instance.template)
        
        c = template.Context({
            'name': request.user.username,
            'Name' : 'Chanchel',
            
        })
        
        rendered_template = []
        serializer = self.get_serializer(instance)
        serializer_copy_data = serializer.data.copy()
        serializer_copy_data['rendered_template'] = t.render(c)
        return Response(serializer_copy_data)

class CategoryListAPIView(CURDViewSet):
    queryset = Category.objects.filter(status=1, deleted_at=None)
    serializer_class = CategorySerializer

class SubCategoryListAPIView(CURDViewSet):
    queryset = SubCategory.objects.filter(status=1, deleted_at=None)
    serializer_class = SubCategorySerializer






