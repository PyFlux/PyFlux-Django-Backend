from shared.views import CURDViewSet
from library.models import *
from library.serializers import BookCategorySerializer, BooksSerializer, BookStatusSerializer, BookVendorSerializer, \
    CupBoardSerializer, CupBoardShelfSerializer, IssueBookSerializer, FineSerializer, CupboardShelfFieldSerializer
# from rest_framework.permissions import IsAuthenticated  
from django.shortcuts import render
from rest_framework.response import Response
import datetime
from rest_framework.views import APIView


class ReturnRenewBookListAPIView(CURDViewSet):
    queryset = IssueBook.objects.filter(deleted_at=None)
    serializer_class = IssueBookSerializer
    # permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        '''
        If Book Is Returned
        '''

        books = Books.objects.get(pk = request.data['book'])
        if request.data['book_status'] == '0':
            IssueBook.objects.filter(pk = request.data['id']).update(
            return_date = datetime.date.today(),
            book_status = '0')
            #currentbook = 
            books.book_current_count = int(books.book_current_count) + 1
            books.save()

            #currentbook.book_current_count = int(count) + 1;
            #currentbook.save()

        elif request.data['book_status'] == '2':
            IssueBook.objects.filter(pk = request.data['id']).update(
            issue_date = datetime.date.today(),
            book_status = '2')
            

        return Response('test')