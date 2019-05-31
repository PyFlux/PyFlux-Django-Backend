from shared.views import CURDViewSet
from library.models import *
from library.serializers import BookCategorySerializer, BooksSerializer, BookStatusSerializer, BookVendorSerializer, \
    CupBoardSerializer, CupBoardShelfSerializer, IssueBookSerializer, FineSerializer, CupboardShelfFieldSerializer
# from rest_framework.permissions import IsAuthenticated  
from django.shortcuts import render
from rest_framework.response import Response
import datetime

class FineListAPIView(CURDViewSet):
    queryset = Fine.objects.filter(status=1, deleted_at=None)
    serializer_class = FineSerializer
    # permission_classes = (IsAuthenticated,)