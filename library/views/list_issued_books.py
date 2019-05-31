from shared.views import CURDViewSet
from library.models import *
from library.serializers import BookCategorySerializer, BooksSerializer, BookStatusSerializer, BookVendorSerializer, \
    CupBoardSerializer, CupBoardShelfSerializer, IssueBookSerializer, FineSerializer, CupboardShelfFieldSerializer
# from rest_framework.permissions import IsAuthenticated  
from django.shortcuts import render
from rest_framework.response import Response
import datetime
from rest_framework.views import APIView

class ListIssuedBooks(APIView):
    """
    View to list of Books of a perticular Student.
    """
    # permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        queryset = IssueBook.objects.filter(student_id = request.GET['id']).values()
        return Response(queryset)
