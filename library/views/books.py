from shared.views import CURDViewSet
from library.models import *
from library.serializers import BookCategorySerializer, BooksSerializer, BookStatusSerializer, BookVendorSerializer, \
    CupBoardSerializer, CupBoardShelfSerializer, IssueBookSerializer, FineSerializer, CupboardShelfFieldSerializer
# from rest_framework.permissions import IsAuthenticated  
from django.shortcuts import render
from rest_framework.response import Response
import datetime
from rest_framework.views import APIView



class BooksListAPIView(CURDViewSet):
    queryset = Books.objects.filter(status=1, deleted_at=None)
    serializer_class = BooksSerializer
    # permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        book = Books.objects.create(
            book_name = request.data['book_name'],
            book_category_id =  request.data.get('book_category',''),
            book_subtitle = request.data.get('book_subtitle',''),
            book_author = request.data.get('book_author',''),
            book_isbn_no = request.data.get('book_isbn_no',''),
            book_cupboard_shelf_id = request.data['book_cupboard_shelf'],
            book_edition = request.data.get('book_edition',''),
            book_publisher = request.data.get('book_publisher',''),
            book_cost = request.data['book_cost'],
            book_vendor_id = request.data.get('book_vendor',''),
            book_count = request.data['book_count'],
            book_current_count = request.data['book_count'],
            book_remarks = request.data.get('book_remarks',''),
            status = request.data['status'])
        BookStatus.objects.create(book_id = book.id,status = 1)

        return Response('test')

    def update(self, request, *args, **kwargs):
        Books.objects.filter(pk = request.data['id']).update(
            book_name = request.data['book_name'],
            book_category_id =  request.data['book_category'],
            book_subtitle = request.data['book_subtitle'],
            book_author = request.data['book_author'],
            book_isbn_no = request.data['book_isbn_no'],
            book_cupboard_shelf_id = request.data['book_cupboard_shelf'],
            book_edition = request.data['book_edition'],
            book_publisher = request.data['book_publisher'],
            book_cost = request.data['book_cost'],
            book_vendor_id = request.data['book_vendor'],
            book_count = request.data['book_count'],
            book_current_count = request.data['book_count'],
            book_remarks = request.data.get('book_remarks',''),
            status = request.data['status'])
        BookStatus.objects.update_or_create(book_id = request.data['id'],
          status = 1)

    
        return Response('test')


