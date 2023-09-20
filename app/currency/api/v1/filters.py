import django_filters
from currency.models import Rate, ContactUs


class RateFilter(django_filters.FilterSet):

    class Meta:
        model = Rate
        fields = {
            'buy': ('gt', 'gte', 'lt', 'lte', 'exact'),
            'sell': ('gt', 'gte', 'lt', 'lte', 'exact'),
            'currency': ('exact',),
        }


class ContactFilter(django_filters.FilterSet):

    class Meta:
        model = ContactUs
        fields = {
            'email_from': ('exact',),
            'subject': ('exact',),
            'message': ('exact',),
        }
