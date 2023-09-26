from rest_framework import viewsets, generics
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework_yaml.renderers import YAMLRenderer

from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters

from currency.models import Rate, Source, ContactUs
from currency.api.v1.serializers import (RateSerializer, SourceSerializer, ContactSerializer)
from currency.api.v1.paginations import DefaultPagination
from currency.api.v1.filters import RateFilter, ContactFilter


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


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all().order_by('-id')
    serializer_class = ContactSerializer
    pagination_class = DefaultPagination
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_framework_filters.OrderingFilter,
    )
    filterset_class = ContactFilter
    ordering_fields = ('email_from', 'subject', 'message')


class ContactDetailApiView(generics.RetrieveDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = ContactUs.objects.all()


class SourceDetailApiView(generics.RetrieveDestroyAPIView):
    serializer_class = SourceSerializer
    queryset = Source.objects.all()
