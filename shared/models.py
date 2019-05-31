from django.db import models
from rest_framework import serializers
from collections import OrderedDict
#from dashboard.models import Users

class SoftDeleteManager(models.Manager):
    def get_query_set(self):
        query_set = super(SoftDeleteManager, self).get_query_set()
        return query_set.filter(deleted_at__isnull = True)

class BaseModelManager(models.Manager):
    def filter_queryset(self, qs,params = None):
        return qs

    def render_column(self, row, column, request = None):
        # this is required since datatable will 
        # call: self.model.filter_objects.render_column(row=row, column=column)
        return False

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)
    # created_by = models.IntegerField(null=True)
    created_by = models.ForeignKey('dashboard.Users', 
        on_delete= models.CASCADE, 
        related_name='%(app_label)s_%(class)s_created_by', null=True) #
    updated_by = models.ForeignKey('dashboard.Users', 
        on_delete= models.CASCADE, 
        related_name='%(app_label)s_%(class)s_updated_by', null=True) #
    objects = models.Manager() # The default manager.
    filter_objects = BaseModelManager()
    class Meta:
        abstract = True

    # def save(self,*args, **kwargs):
    #     print(request,args,kwargs)
    #     super().save(*args, **kwargs)

# abstracted serializer
def serializer_factory(mdl, fields="__all__", **kwargss):
    # https://stackoverflow.com/a/33137535/2351696
    """
    def _get_declared_fields(attrs):
        fields = [(field_name, attrs.pop(field_name))
                  for field_name, obj in list(attrs.items())
                  if isinstance(obj, Field)]
        fields.sort(key=lambda x: x[1]._creation_counter)
        return OrderedDict(fields)

    # Create an object that will look like a base serializer
    class Base(object):
        pass

    Base._declared_fields = _get_declared_fields(kwargss)
    """
    class MySerializer(serializers.ModelSerializer):
        # created_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
        class Meta:
            model = mdl
        if fields:
            setattr(Meta, "fields", fields) #fields = fields
    return MySerializer