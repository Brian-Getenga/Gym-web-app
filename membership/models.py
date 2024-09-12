from django.db import models
from django.contrib.auth.models import User

class Membership(models.Model):
    MEMBERSHIP_TYPES = [
        ('BASIC', 'Basic'),
        ('PREMIUM', 'Premium'),
        ('VIP', 'VIP'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_type = models.CharField(max_length=10, choices=MEMBERSHIP_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.membership_type}"