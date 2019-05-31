from django.urls import path, include

from .views import (notifications, ) 

urlpatterns = [
	path('notifications/', notifications.NotificationView.as_view()),
]
