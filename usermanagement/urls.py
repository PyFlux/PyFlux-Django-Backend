from .views import (assignments, fees, profile, feedback,documents,
    verify_email, verify_mobile)
from django.urls import path, include, re_path

urlpatterns = [    

    path('profile/', profile.ProfilePage.as_view(), name = 'profilepage' ),
    path('getfeetransactions/', fees.getFeeTransactions.as_view()),
    path('getuserprofile/', profile.GetUserProfile.as_view()),
    path('edituserprofile/', profile.EditUserProfile.as_view()),
    path('edituseraddress/', profile.EditUserAddress.as_view()),    
    path('assignment/',assignments.getAssignment.as_view()),
    path('assignmentactivestatus/',assignments.AssignmentActiveStatus.as_view()),
    path('assignmentinactivestatus/',assignments.AssignmentInActiveStatus.as_view()),
    path('assignmentinprogressstatus/',assignments.AssignmentInProgressStatus.as_view()),
    path('assignmentcompletedstatus/',assignments.AssignmentCompletedStatus.as_view()),
    # path('assignmentteacher/',assignments.getTeacherAssignment.as_view()),

    path('changefeedback/',feedback.ChangeFeedback.as_view()),
    path('feedbackresolvedstatus/',feedback.FeedbackResolvedStatus.as_view()),
    path('feedbackclosedstatus/',feedback.FeedbackClosedStatus.as_view()),
    path('getdocuments/',documents.getDocuments.as_view()),

    # path('sendemailverification/',activate_email.SendEmailVerificationView.as_view()),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     activate_email.activate, name='activate_email'),
    path('sendemailverification/',verify_email.SendVerificationView.as_view()),
    re_path(r'^verifyemail/(?P<key>[-:\w]+)/$', verify_email.VerifyEmail.as_view()),

    path('sendmobileverification/', verify_mobile.SendVerificationView.as_view()),
    path('verifymobile/', verify_mobile.VerifyMobile.as_view()),
]
