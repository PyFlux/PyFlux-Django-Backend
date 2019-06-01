from .views import (profile, feedback,
    verify_email, verify_mobile)
from django.urls import path, include, re_path

urlpatterns = [
    path('profile/', profile.ProfilePage.as_view(), name = 'profilepage' ),
    path('getuserprofile/', profile.GetUserProfile.as_view()),
    path('edituserprofile/', profile.EditUserProfile.as_view()),
    path('edituseraddress/', profile.EditUserAddress.as_view()),
    path('changefeedback/',feedback.ChangeFeedback.as_view()),
    path('feedbackresolvedstatus/',feedback.FeedbackResolvedStatus.as_view()),
    path('feedbackclosedstatus/',feedback.FeedbackClosedStatus.as_view()),
    path('sendemailverification/',verify_email.SendVerificationView.as_view()),
    re_path(r'^verifyemail/(?P<key>[-:\w]+)/$', verify_email.VerifyEmail.as_view()),
    path('sendmobileverification/', verify_mobile.SendVerificationView.as_view()),
    path('verifymobile/', verify_mobile.VerifyMobile.as_view()),
]
