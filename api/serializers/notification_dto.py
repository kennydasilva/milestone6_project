from rest_framework import serializers
from api.models import Notification

class NotificationCreateDTO(serializers.Serializer):
    title=serializers.CharField(max_length=255)
    message=serializers.CharField()
    email=serializers.EmailField()

class NotifictionResponseDTO(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields='__all__'