from django.db import models

from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class BooksManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'book_name':
                q |= Q(book_name__icontains=search)
            
            if col == 'book_category.book_category':
                q |= Q(book_category__book_category__icontains=search)
            
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column, request):
        return False


class Books(BaseModel):
    class Meta:
        db_table = '"library_books_info"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    book_name = models.CharField(max_length=255, null=True)
    book_category = models.ForeignKey('library.BookCategory', on_delete=models.CASCADE, null=True)
    book_subtitle = models.CharField(max_length=255, null=True)
    book_author = models.CharField(max_length=255, null=True)
    book_isbn_no = models.CharField(max_length=255, null=True)
    book_cupboard_shelf = models.ForeignKey('library.CupboardShelfField', on_delete=models.CASCADE, null=True)
    book_edition = models.CharField(max_length=255, null=True)
    book_publisher = models.CharField(max_length=255, null=True)
    book_cost = models.IntegerField(null=True)
    book_vendor =models.ForeignKey('library.BookVendor', on_delete=models.CASCADE, null=True)
    book_count = models.IntegerField(null=True)
    book_current_count = models.IntegerField(blank=True, null=True)
    book_remarks = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField(default=1)

    

    columns = ['id','book_name','book_category.book_category','book_author','status']
    order_columns = ['id','book_name','book_category.book_category','book_author','status','']

    objects = models.Manager() # The default manager.
    filter_objects = BooksManager()

    def __str__(self):
        return "%s" % (self.book_name)