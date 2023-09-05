from django.urls import path

from account.views import SignUpView, UserActivationView, ProfileView

app_name = 'account'

urlpatterns = [
   path('signup/', SignUpView.as_view(), name='signup'),
   path('activate/<uuid:username>', UserActivationView.as_view(), name='activate'),
   path("auth/profile/", ProfileView.as_view(), name='profile'),

]
