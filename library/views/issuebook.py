from shared.views import CURDViewSet
from library.models import *
from library.serializers import BookCategorySerializer, BooksSerializer, BookStatusSerializer, BookVendorSerializer, \
    CupBoardSerializer, CupBoardShelfSerializer, IssueBookSerializer, FineSerializer, CupboardShelfFieldSerializer
# from rest_framework.permissions import IsAuthenticated  
from django.shortcuts import render
from rest_framework.response import Response
import datetime


class IssueBookListAPIView(CURDViewSet):
    queryset = IssueBook.objects.filter(deleted_at=None)
    serializer_class = IssueBookSerializer
    # permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        
        IssueBook.objects.create(
        book_id = request.data['book'],
        created_by = request.user,
        student_id = request.data['student'],
        issue_date = datetime.date.today(),
        return_date = datetime.date.today() + datetime.timedelta(days=14),
        book_status = '1')
        currentbook = Books.objects.get(pk = request.data['book'])
        count = currentbook.book_current_count
        currentbook.book_current_count = int(count) - 1;
        currentbook.save()
        
        
        return Response('test')
    
    def update(self, request, *args, **kwargs):
        '''
        increment count of previous book
        '''
        issuedbook =  IssueBook.objects.get(id = request.data['id'])
        #previousbook = Books.objects.get(pk = issuedbook.book)
        count = issuedbook.book.book_current_count
        issuedbook.book.book_current_count = int(count) + 1;
        issuedbook.book.save()

        '''
        update book
        '''
        IssueBook.objects.filter(pk = request.data['id']).update(
        book_id = request.data['book'],
        student_id = request.data['student'],
        issue_date = datetime.date.today(),
        updated_by = request.user,
        return_date = datetime.date.today() + datetime.timedelta(days=14),
        book_status = '1')
        currentbook = Books.objects.get(pk = request.data['book'])
        count = currentbook.book_current_count
        currentbook.book_current_count = int(count) - 1;
        currentbook.save()
        
        
        return Response('test')