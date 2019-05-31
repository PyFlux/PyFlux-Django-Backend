from django.shortcuts import render
    
from rest_framework import parsers
from rest_framework import response
from rest_framework.response import Response

from dashboard.models import *

from students.models import Student;

from rest_framework.views import APIView
from parents.models import Parents
import datetime
from notifications.views.pushnotifications import FCMNotifications
from django.utils.timezone import datetime as dt


class PushNotification(APIView):
   '''
   when attendence marked notifications for parent

   '''
   def attendance_notifications(absenties,myclass):
        # https://stackoverflow.com/questions/7503241/django-models-selecting-single-field
        class_students = list(Student.objects.filter(myclass_id = myclass).values_list('user_id', flat=True))
        presenties = list(set(class_students).difference(set(absenties)))

        for stu in presenties:
            student = Users.objects.get(id=stu)
            parents = Parents.objects.filter(student = student)
            message = '{} is Marked as Present on today'.format(str(student.full_name))
            data = {'title':'Attendence','body':message,
            'data':{'title':'Attendence','body':message,'redirect_type':1}}
            for par in parents: 
                FCMNotifications.send_notifications(par.user,data)
        
        for stu in absenties:
            student = Users.objects.get(id=stu)
            parents = Parents.objects.filter(student = student)
            message = '{} is Marked as Absent on today'.format(str(student.full_name))
            data = {'title':'Attendence','body':message,
            'data':{'title':'Attendence','body':message,'redirect_type':1}}
            for par in parents: 
                FCMNotifications.send_notifications(par.user,data)
    

   def markentry_notifications(myclass,exam):
        # https://stackoverflow.com/questions/7503241/django-models-selecting-single-field
        class_students = Student.objects.filter(myclass_id = myclass)

        for stu in class_students:
            parents = Parents.objects.filter(student = stu.user)
            message = '{} {} Marks Published.'.format(str(stu.user.full_name),exam)
            data = {'title':'Exams','body':message,
            'data':{'title':'Exams','body':message,'redirect_type':1}}
            for par in parents: 
                FCMNotifications.send_notifications(par.user,data)
        