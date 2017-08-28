from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from notifications.api.serializers import NotificationListSerializer
from notifications.models import Notification


class NotificationListAPIView(ListAPIView):
    def get(self, request, username):
        # queryset = self.filter_queryset(self.get_queryset())

        # serializer = self.get_serializer(queryset, many=True)

        print(username)

        notifications = Notification.objects.filter(from_user__username=username)

        serializer = NotificationListSerializer(notifications, many=True)

        serializer_data = serializer.data

        custom_data = {'notifications': serializer_data}

        return Response(custom_data)