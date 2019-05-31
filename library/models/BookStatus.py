from django.db import models
from library.models import Books
from library.models.IssueBook import IssueBook
from django.utils import timezone

from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class BookStatusManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'book.book_name':
                q |= Q(book__book_name__icontains=search)
            
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column, request):
        return False


class BookStatus(BaseModel):
    class Meta:
        db_table = '"library_book_status"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    book= models.ForeignKey('library.Books', on_delete=models.CASCADE, null=True)
    

    # book_details = models.CharField(max_length=255 , blank=True, null=True)

    status = models.SmallIntegerField(default=1)

    @property
    def get_duebooks(self):
        
        today = timezone.now()
        count = 0
        # print(IssueBook.IssueBook)
        duebooks = IssueBook.objects.filter(book_id = self.book.id,return_date__gte = today,book_status__in =['1','2'] ).values().count()
        
        return(duebooks)


    @property
    def get_issuedbooks(self):

        return(self.book.book_count-self.book.book_current_count )
    


    columns = ['id','book.book_name','book.book_count','get_issuedbooks','get_duebooks']
    order_columns = ['id','book.book_name','','','']
    
    objects = models.Manager() # The default manager.
    filter_objects = BookStatusManager()