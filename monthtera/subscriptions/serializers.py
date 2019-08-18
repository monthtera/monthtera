from rest_framework import serializers
from .models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('item', 'user', 'start_date', 'is_alarm', 'when_alarm', 'note')
