from django.urls import path
from .views import subscribe, unsubscribe, list_subscriptions, report_history

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('unsubscribe/', unsubscribe, name='unsubscribe'),
    path('subscriptions/', list_subscriptions, name='list_subscriptions'),
    path('reports/history/', report_history, name='report_history'),
]