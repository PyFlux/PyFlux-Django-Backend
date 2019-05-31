from rest_framework import routers
from systemconfig.views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'citytown', citytown.CityTownListAPIView)
router.register(r'country', country.CountryListAPIView)
router.register(r'caste', caste.CasteListAPIView)
router.register(r'district', district.DistrictListAPIView)
router.register(r'emailconfig', emailconfig.EmailConfigListAPIView)
router.register(r'languages', language.LanguagesListAPIView)
router.register(r'nationality', nationality.NationalityListAPIView)
router.register(r'occupation', occupation.OccupationListAPIView)

router.register(r'organization', organization.OrganizationListAPIView)
router.register(r'relationship', relationship.RelationshipListAPIView)
router.register(r'religion', religion.ReligionListAPIView)
router.register(r'smsconfig', smsconfig.SmsConfigListAPIView)
router.register(r'state', state.StateListAPIView)
router.register(r'hobby', hobby.HobbyListAPIView)
router.register(r'emailcredentials', emailcredential.EmailCredentialsListAPIView)
router.register(r'smscredentials', smscredential.SmsCredentialsListAPIView)
router.register(r'clubinformation', clubinfo.ClubInfoListAPIView)
urlpatterns = [
    path('', include(router.urls)),
    path('getactiveorganization/', organization.GetActiveOrganization.as_view()),
    path('getcaste_religion/', caste.GetCastes.as_view()),
]