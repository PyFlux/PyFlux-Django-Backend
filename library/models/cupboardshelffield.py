from django.db import models
from shared.models import BaseModel

class CupboardShelfField(BaseModel):
    class Meta:
        db_table = '"library_book_cupboardshelf_field"'
   
    cupboard= models.ForeignKey('library.CupBoard', on_delete=models.CASCADE, related_name = 'cupboardfields', null=True)
    cupboard_shelf_name = models.CharField(max_length=255, null=True)
    status = models.IntegerField(null=True)

    
    



