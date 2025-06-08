from celery import shared_task
from django.core.mail import EmailMessage
from django.utils import timezone
from .models import Subscription, ReportHistory
from .utils import generate_pdf_report, generate_html_report
import datetime

@shared_task
def send_daily_reports():
    today = timezone.now().date()
    subscriptions = Subscription.objects.filter(start_date__lte=today, end_date__gte=today)

    for subscription in subscriptions:
        user_email = subscription.user.email
        report_data = {
            'date': today,
            'summary': f'Daily Summary for {today}',
            # Add more mock data as needed
        }

        # Generate reports
        pdf_report = generate_pdf_report(report_data)
        html_report = generate_html_report(report_data)

        # Send email with reports
        email = EmailMessage(
            subject=f'Daily Report for {today}',
            body='Please find attached your daily report.',
            to=[user_email]
        )
        email.attach(f'daily_report_{today}.pdf', pdf_report, 'application/pdf')
        email.attach(f'daily_report_{today}.html', html_report, 'text/html')
        email.send()

        # Log the report history
        ReportHistory.objects.create(user=subscription.user, date=today, report_type='PDF/HTML')