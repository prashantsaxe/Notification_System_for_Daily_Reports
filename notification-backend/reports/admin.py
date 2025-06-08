from django.contrib import admin
from .models import Subscription, ReportHistory

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'formats', 'is_active')
    search_fields = ('user__username',)
    list_filter = ('is_active',)

@admin.register(ReportHistory)
class ReportHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'report_date', 'format', 'sent_at')
    search_fields = ('user__username',)
    list_filter = ('format',)