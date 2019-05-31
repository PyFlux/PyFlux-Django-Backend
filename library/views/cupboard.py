from shared.views import CURDViewSet
from rest_framework.views import APIView
from library.models import *
from library.serializers import BookCategorySerializer, BooksSerializer, BookStatusSerializer, BookVendorSerializer, \
    CupBoardSerializer, CupBoardShelfSerializer, IssueBookSerializer, FineSerializer, CupboardShelfFieldSerializer
# from rest_framework.permissions import IsAuthenticated  
from django.shortcuts import render

from rest_framework.response import Response
import datetime

class CupBoardListAPIView(CURDViewSet):
    queryset = CupBoard.objects.filter(status=1, deleted_at=None)
    serializer_class = CupBoardSerializer
    # permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
       

        cupboard = CupBoard.objects.create(
            cupboard_name = request.data['cupboard_name'])
            
        
        cupboardshelffields = request.data['units']
        for field in cupboardshelffields: 
            CupboardShelfField.objects.create(
                cupboard = cupboard, 
                cupboard_shelf_name = field['cupboard_shelf_name'])
        return Response('test')
    

    def update(self, request, *args, **kwargs):
        
        cupboard = CupBoard.objects.get(pk = request.data['id'])
        cupboard.cupboard_name = request.data['cupboard_name']
        
        cupboard.save()

        queryset = CupboardShelfField.objects.filter(cupboard_id = request.data['id']).values()
        CupboardShelfField.objects.filter(cupboard_id = cupboard).delete()
        cupboardshelffields = request.data['units']
        for field in cupboardshelffields: 
            CupboardShelfField.objects.create(
                cupboard = cupboard, 
                cupboard_shelf_name = field['cupboard_shelf_name'])
        return Response('test')


class GetCupboardshelfname(APIView):


     def get(self, request, format=None):

        queryset =  CupBoard.objects.all()
        shelf_list = []
        for query in queryset.values():
            cupboardname  = query['cupboard_name']
            cupboard_id = query['id']
            queryset2 = CupboardShelfField.objects.filter(cupboard_id = cupboard_id)
            
            for query2 in queryset2:
                cupboard_shelf = "%s-%s" %(query['cupboard_name'],query2.cupboard_shelf_name )
                shelf_list.append({'cupboard_shelf':cupboard_shelf,'id':query2.id})
                
        return Response(shelf_list)
