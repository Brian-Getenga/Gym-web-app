from django.db import models
from django.contrib.auth.models import User

class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.user.username

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_earned = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.title}"