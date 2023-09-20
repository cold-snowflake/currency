from rest_framework import serializers

from currency.models import Rate, Source, ContactUs
from currency.tasks import send_email_to_background


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


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message')

        def create(self, validated_data):
            return ContactUs(**validated_data)

        def update(self, instance, validated_data):
            instance.email_from = validated_data.get('email_from', instance.email_from)
            instance.subject = validated_data.get('subject', instance.subject)
            instance.message = validated_data.get('message', instance.message)
            send_email_to_background.apply_async(validated_data)
            return instance
