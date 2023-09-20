from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

from currency.models import Rate, Source
from currency.api.v1.serializers import RateSerializer, SourceSerializer
from currency.api.v1.paginations import DefaultPagination
from currency.api.v1.filters import RateFilter


class RatesViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer
    renderer_classes = (JSONRenderer, XMLRenderer, YAMLRenderer)
    pagination_class = DefaultPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = RateFilter
    ordering_fields = ('buy', 'sell', 'created')


class SourcesViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
