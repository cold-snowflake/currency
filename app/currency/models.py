from django.db import models
from django.utils.translation import gettext_lazy as _
from currency.choices import RateCurrencyChoices


class Rate(models.Model):
    buy = models.DecimalField(_('Buy'), max_digits=6, decimal_places=2)
    sell = models.DecimalField(_('Sell'), max_digits=6, decimal_places=2)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        _('Currency'),
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD)
    source = models.CharField(_('Source'), max_length=68)

    class Meta:
        verbose_name = _('Rate')
        verbose_name_plural = _('Rates')


class ContactUs(models.Model):
    email_from = models.EmailField(blank=False)
    subject = models.CharField(max_length=25)
    message = models.CharField(max_length=250)


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
