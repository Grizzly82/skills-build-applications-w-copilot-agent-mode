from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.PositiveIntegerField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)  # Height in cm
    weight = models.FloatField(null=True, blank=True)  # Weight in kg
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50)  # e.g., Running, Walking, Strength Training
    duration = models.PositiveIntegerField()  # Duration in minutes
    distance = models.FloatField(null=True, blank=True)  # Distance in kilometers (optional)
    calories_burned = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} on {self.timestamp}"