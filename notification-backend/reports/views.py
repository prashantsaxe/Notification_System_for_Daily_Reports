from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Subscription, ReportHistory
from .serializers import SubscriptionSerializer, ReportHistorySerializer
from django.utils import timezone

class SubscriptionView(APIView):
    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            subscription = serializer.save()
            return Response(SubscriptionSerializer(subscription).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        subscription_id = request.data.get('id')
        try:
            subscription = Subscription.objects.get(id=subscription_id)
            subscription.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Subscription.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class SubscriptionListView(APIView):
    def get(self, request):
        subscriptions = Subscription.objects.filter(user=request.user)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

class ReportHistoryView(APIView):
    def get(self, request):
        report_history = ReportHistory.objects.filter(user=request.user)
        serializer = ReportHistorySerializer(report_history, many=True)
        return Response(serializer.data)