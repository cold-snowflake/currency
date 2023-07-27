from django.urls import path

from currency.views import (
    RateListView, RateCreateView, RateUpdateView, RateDetailView, RateDeleteView,
    ContactListView, ContactCreateView, ContactUpdateView, ContactDeleteView, ContactDetailView,
    SourceListView, SourceCreateView, SourceUpdateView, SourceDeleteView, SourceDetailView,
    RequestResponseLogView,
)

app_name = 'currency'

urlpatterns = [
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('contact/list/', ContactListView.as_view(), name='contact-list'),
    path('contact/create/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/update/<int:pk>', ContactUpdateView.as_view(), name='contact-update'),
    path('contact/delete/<int:pk>', ContactDeleteView.as_view(), name='contact-delete'),
    path('contact/details/<int:pk>', ContactDetailView.as_view(), name='contact-detail'),
    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
    path('source/details/<int:pk>/', SourceDetailView.as_view(), name='source-detail'),
    path('request/response/log', RequestResponseLogView.as_view(), name='request-response-log')

]
