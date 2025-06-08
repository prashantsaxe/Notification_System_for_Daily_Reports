from django.db import models
from django.contrib.auth.models import User

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    formats = models.CharField(max_length=10)  # e.g., 'PDF', 'HTML', 'Both'
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.formats} from {self.start_date} to {self.end_date}"

class ReportHistory(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    report_date = models.DateField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.report_date} sent at {self.sent_at}"