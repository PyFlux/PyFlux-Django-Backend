from django.db import models
from django.db.models.functions import Concat
from django.db.models import Value

from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class IssueBookManager(BaseModelManager):
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
            
            if col == 'student.first_name':
                q |= Q(student__first_name__icontains=search)
            
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column, request):
        return False


CHOICES = (
     ('0', 'Returned'),
     ('1','Issued'),
     ('2','Renewed'),
   
)


class IssueBook(BaseModel):
    class Meta:
        db_table = '"library_issue_book"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    book = models.ForeignKey('library.Books', on_delete=models.CASCADE, related_name='issuebooks', null=True)
    student = models.ForeignKey('dashboard.Users', on_delete=models.CASCADE, related_name='Student_id', null=True)
    issue_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    book_status = models.CharField(max_length=6, choices=CHOICES, null=True)
    count = models.IntegerField(null = True)
    # return_renew_status = models.CharField(blank=True, max_length=6, choices=Return_Renew_choice)
    
    columns = ['id','book.book_name','student.first_name','book_status']
    order_columns = ['id','book.book_name','student.first_name','book_status','']

    objects = models.Manager() # The default manager.
    filter_objects = IssueBookManager()