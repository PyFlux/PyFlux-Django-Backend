from django.db import models
from django.conf import settings
from django.db.models import Q
from shared.models import BaseModel, BaseModelManager
import datetime
# from utils.file_upload import *
class TemplateManager(BaseModelManager):   

    def filter_search(self, qs, search):
        """
        To search from given string in the search box on the datatable.
        """
        if not search: return qs

        q = Q()
        for col in self.model.order_columns:
            # skip non searchable columns
            if col in ['', 'id', 'status']: continue

            if col == 'category':
                q |= Q(category__icontains=search)
            if col == 'subcategory':
                q |= Q(subcategory__icontains=search)
           
            else:
                # apply global search to all searchable columns
                q |= Q(**{'{0}__istartswith'.format(col.replace('.', '__')): search})

        return qs.filter(q)


    def filter_queryset(self, qs, params): 
        qs = self.filter_search(qs,params['search'])
        return qs

    def render_column(self, row, column,request):
        if column == 'test_template':
            # message_details =Messages.objects.filter(id=row.id).values('message','id')
            template_details =Template.objects.filter(id=row.id).values()
            template_id = template_details[0]['id']
            # message=message_details[0]['message']
            return '''
                <center>
                <a class="btn btn-default btn-xs navigate_button" 
                    data-link="/utils/templates/view/" data-param="{template_id}">
                    <i class="fa fa-check-circle"></i> Test Template
                </a>
                </center>
            '''.format(template_id = row.id)
        return False
class Template(BaseModel):
    class Meta:
        db_table = '"utils_template"'

    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255,blank=True)
    category = models.ManyToManyField('utils.Category',blank=True)
    subcategory = models.ManyToManyField('utils.SubCategory',blank=True)
    template = models.TextField(null=True)
    test_template= models.CharField(max_length=255, null=True)
    status = models.SmallIntegerField(default=1)

    def __str__(self):
        return "%s" % (self.name)

    objects = models.Manager() # The default manager.
    filter_objects = TemplateManager()

    columns = ['id','name','get_category','get_subcategory','status','test_template']
    order_columns = ['id','name','get_category','get_subcategory','status','test_template']
    
    @property
    def get_category(self):
        return ", ".join([s.category for s in self.category.all()])

    @property
    def get_subcategory(self):
        return ", ".join([s.subcategory for s in self.subcategory.all()])
    

   