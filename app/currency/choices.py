from django.utils.translation import gettext_lazy as _
from django.db import models


class RateCurrencyChoices(models.IntegerChoices):
    EUR = 1, _('Dollar')
    USD = 2, _('Euro')
