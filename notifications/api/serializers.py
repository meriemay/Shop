from rest_framework.serializers import ModelSerializer, SerializerMethodField

from notifications.models import Notification


class NotificationListSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'type', 'date', 'is_read')