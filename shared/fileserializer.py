from rest_framework import serializers
import os
from django.conf import settings
from itertools import chain 
class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if '/media/' in data:
            # image already exist
            
            return data.split('/media/')[1]
        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # file_name = student # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)
        
        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension


# class Base64FileField(serializers.FileField):

#     def to_representation(self, value):
#         import base64
#         # when deriving from serializers.SerializerMethodField, use:
#         # filefield = getattr(value, self.field_name)
#         print("hhhhhhhhhhhhhhhhhhhhhhhh")
#         print(value)
#         filefield = value

#         if bool(filefield):
#             data = {
#                 'filename': os.path.split(filefield.name)[-1],
#                 'data': filefield.file.read().encode('base64'),
#             }
#         else:
#             data = None

#         return data

#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64

        
#         print(data)
#         content_file = ContentFile(
#             base64.b64decode(data['data']),
#             name=data['filename']
#         )
#         return content_file
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """
class Base64FileField(serializers.FileField):
    
    def to_internal_value(self,data):
        # filename = os.path.split(data.name)[-1],
        # print(filename)
        
        print(data.split('.')[0])
        file_name = data.split('.')[0]
        file_extension = self.get_file_extension(data)
        # start_sep = '/'
        # end_sep='.'
        # filename=[]
        # tmp=data.split(start_sep)
        # for par in tmp:
        #   if end_sep in par:
        #     filename.append(par.split(end_sep)[0])

        #     print(filename)
        
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if '/media/' in data:
            # image already exist
            
            return data.split('/media/')[1]
        # Check if this is a base64 string
        if isinstance(data, six.string_types):

            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content

                header, data = data.split(';base64,')


            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_file')


            # Generate file name:
            # file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # file_name = student # 12 characters are more than enough.
            # Get the file name extension:
            print(file_name)
            
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            print(complete_file_name)

            data = ContentFile(decoded_file, name=complete_file_name)
        
        return super(Base64FileField, self).to_internal_value(data)

    def get_file_extension(self,data):

        start_sep='/'
        end_sep=';'
        extension=[]
        tmp=data.split(start_sep)
        for par in tmp:
          if end_sep in par:
            extension.append(par.split(end_sep)[0])
            return extension
        

    