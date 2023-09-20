from rest_framework.routers import DefaultRouter

from currency.api.views import (
    RatesViewSet
)

app_name = 'currency_api'

router = DefaultRouter(trailing_slash=False)
router.register('rates/', RatesViewSet, basename='rates')

urlpatterns = [
] + router.urls
