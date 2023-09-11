import django_filters
from currency.models import Rate, ContactUs


class RateFilter(django_filters.FilterSet):

    class Meta:
        model = Rate
        fields = (
            'buy',
            'sell',
            'currency',
        )


class ContactUsFilter(django_filters.FilterSet):

    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message',
        )
