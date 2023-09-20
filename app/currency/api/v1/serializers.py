from rest_framework import serializers

from currency.models import Rate, Source


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sell',
            'created',
            'source',
            'currency'
        )


class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = (
            'source_url',
            'name'
        )
