from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from shared.fileserializer import Base64ImageField

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        # validate_password(value)
        if len(value) < 3:
            raise serializers.ValidationError('New Password must have atleast 3 characters.')
        return value

    def validate(self, data):
        if data.get('new_password') != data.get('confirm_password'):
            raise serializers.ValidationError("Password confirmation doesn't match the password.")
        # if len(data.get('new_password')) < 3:
        #      raise serializers.ValidationError('New Password must have atleast 3 characters.')
        return data

class EditUserProfileSerializer(serializers.Serializer):
    email = serializers.CharField()
    first_name = serializers.CharField()
    middle_name = serializers.CharField()
    last_name = serializers.CharField()
    dob = serializers.CharField()
    personal_mobile_no = serializers.CharField()
    #media = serializers.ImageField()
    media = Base64ImageField(
       max_length=None, use_url=True, required=False
    )