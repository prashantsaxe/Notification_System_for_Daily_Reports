from rest_framework import serializers
from .models import Subscription, ReportHistory

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'start_date', 'end_date', 'formats', 'is_active']

class ReportHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportHistory
        fields = ['id', 'user', 'report_date', 'formats', 'status']