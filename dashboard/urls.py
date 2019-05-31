from django.urls import path, include
from rest_framework import routers

from shared.views import CURDViewSet

from dashboard.views import curdviews, widgets, accesspermissions, generalsettings, menus, configdetail
from . import models

router = routers.DefaultRouter()

# router.register(r'aclpermission', curdviews.AclPermissionListAPIView)
router.register(r'roles', curdviews.RolesListAPIView)
router.register(r'userprofiles', curdviews.UserProfilesListAPIView)
router.register(r'userroles', curdviews.UserRolesListAPIView)
router.register(r'users', curdviews.UsersListAPIView)
router.register(r'configdetail', configdetail.ConfigDetailListAPIView)

# router.register(r'widgets', CURDViewSet.create_custom(model=models.Widget))
urlpatterns = [
    path('', include(router.urls)),
    path('dashboard_menus/', accesspermissions.DashboardMenu.as_view(), name = 'dashboard_menus' ),
    path('subsubmenudetails/', accesspermissions.getSubSubmenuDetails.as_view()),
    path('get_userwidgets/',widgets.getuserWidgets.as_view()),
    path('get_fullcalendarevents/',widgets.getFullCalenderEvents.as_view()),
    path('rolewidgets/', widgets.getRoleWidgets.as_view()),
    path('usersbirthdays/',widgets.getUserBirthdays.as_view()),
    path('savegeneralsetting/',generalsettings.saveGeneralSetting.as_view()),
    path('getgeneralsettings/',generalsettings.getGeneralSettings.as_view()),
    path('syncmenus/',menus.SyncMenus.as_view()),
]
