from django.db import models

from shared.models import BaseModel, BaseModelManager
from django.db.models import Q

class CupBoardShelfManager(BaseModelManager):
    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'cupboard_shelf_name':
                q |= Q(cupboard_shelf_name__icontains=search)
            
            if col == 'cupboard_name.cupboard_name':
                q |= Q(cupboard_name__cupboard_name__icontains=search)
            
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column, request):
        return False


class CupBoardShelf(BaseModel):
    class Meta:
        db_table = '"library_book_cupboard_shelf"'
    # firm_id = models.IntegerField(null=True)
    # dept_id = models.IntegerField(null=True)
    # org_id = models.IntegerField(null=True)
    cupboard_shelf_name = models.CharField(max_length=255, null=True)
    cupboard_name = models.ForeignKey('library.CupBoard', on_delete=models.CASCADE, null=True)
    cupboardshelf_capacity = models.CharField(max_length=255, null=True)
    cupboardshelf_details = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField(default=1)

    columns = ['id','cupboard_shelf_name','cupboard_name.cupboard_name','cupboardshelf_capacity','status']
    order_columns = ['id','cupboard_shelf_name','cupboard_name.cupboard_name','cupboardshelf_capacity','status','']
    
    objects = models.Manager() # The default manager.
    filter_objects = CupBoardShelfManager()