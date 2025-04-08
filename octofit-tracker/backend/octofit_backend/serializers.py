from rest_framework import serializers
from .models import UserProfile, ActivityLog

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'age', 'height', 'weight', 'bio']
        read_only_fields = ['user']

class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = ['id', 'user', 'activity_type', 'duration', 'distance', 'calories_burned', 'timestamp']
        read_only_fields = ['user', 'timestamp']
