from rest_framework.routers import DefaultRouter

from app.currency.api.v1.views import (
    RatesViewSet, SourcesViewSet
)

app_name = 'currency_api'

router = DefaultRouter(trailing_slash=False)
router.register('rates/', RatesViewSet, basename='rates')
router.register('sources/', SourcesViewSet, basename='sources')

urlpatterns = [
] + router.urls
