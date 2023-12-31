import django_filters
from currency.models import Rate, ContactUs, Source


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


class SourceFilter(django_filters.FilterSet):

    class Meta:
        model = Source
        fields = (
            'source_url',
            'name',
        )
