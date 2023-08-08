from django.urls import path

from account.views import SignUpView, UserActivationView

app_name = 'account'

urlpatterns = [
   path('signup/', SignUpView.as_view(), name='signup'),
   path('activate/<uuid:username>', UserActivationView.as_view(), name='activate')
]
