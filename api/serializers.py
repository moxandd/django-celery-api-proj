from rest_framework import serializers
from core.models import Client, Newsletter, Message

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'phone', 'mobile_code', 'tag', 'timezone']

class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['id', 'send_start', 'text_message', 'mobile_code', 'send_end']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'created_at', 'send_status', 'newsletter_id', 'send_to']