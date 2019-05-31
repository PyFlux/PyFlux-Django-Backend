from rest_framework import serializers
from .models import *
from shared.fileserializer import Base64ImageField, Base64FileField


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CityTownSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityTown
        fields = "__all__"


class EmailConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailConfig
        fields = "__all__"


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = "__all__"


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = "__all__"


class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = "__all__"



class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = "__all__"


class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = "__all__"

class CasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caste
        fields = "__all__"


class SmsConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsConfig
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = "__all__"

class EmailCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailCredentials
        fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):
    org_logo = Base64ImageField(
      max_length=None, use_url=True, required=False, allow_empty_file=True,
    )
    institute_image = Base64ImageField(
      max_length=None, use_url=True, required=False, allow_empty_file=True,
    )
    class Meta:
        model = Organization
        fields = "__all__"


class SmsCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsCredentials
        fields = "__all__"


class ClubInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubInfo
        fields = "__all__"


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = "__all__"
