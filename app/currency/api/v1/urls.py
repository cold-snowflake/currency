from django.urls import path
from rest_framework.routers import DefaultRouter

from app.currency.api.v1.views import (
    RatesViewSet, SourcesViewSet, ContactsViewSet, ContactDetailApiView
)

app_name = 'currency_api'

router = DefaultRouter(trailing_slash=False)
router.register('rates/', RatesViewSet, basename='rates')
router.register('sources/', SourcesViewSet, basename='sources')
router.register('contacs/', ContactsViewSet, basename='contacts')

urlpatterns = [
    path("contact/detail-delete/<int:pk>/", ContactDetailApiView.as_view(), name="contact-detail-delete",),
] + router.urls
