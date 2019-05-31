from rest_framework import routers
from utils.views import templates
from django.urls import path, include
from shared.views import CURDViewSet
# sfrom .views import TaskManagementListAPIView,GetTaskUsers,queryTaskUsersByTerm
from utils.views import (taskmanagement,feedback) 

# from utils.views.template import TemplateListAPIView,CategoryListAPIView,SubCategoryListAPIView
router = routers.DefaultRouter()
router.register(r'taskmanagement', taskmanagement.TaskManagementListAPIView)
router.register(r'feedbackmanagement',feedback.FeedbackListAPIView)
router.register(r'templatemanagement',templates.TemplateListAPIView)
router.register(r'category',templates.CategoryListAPIView)
router.register(r'subcategory',templates.SubCategoryListAPIView)


urlpatterns = [
    path('', include(router.urls)), 
    path('gettaskusers/',taskmanagement.GetTaskUsers.as_view()),
    path('getusersbyterm/',taskmanagement.queryTaskUsersByTerm.as_view()), 
    path('getfeedbackdetails/',feedback.Get_Feedback_details.as_view()) 
]