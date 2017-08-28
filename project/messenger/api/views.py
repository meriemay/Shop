from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from project.messenger.api.serializers import MessageListSerializer, MessageSendSerializer
from project.messenger.models import Message
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )

class MessageListAPIView(ListAPIView):
    def get(self, request, username, format=None):
        # queryset = self.filter_queryset(self.get_queryset())

        # serializer = self.get_serializer(queryset, many=True)

        print(username)

        messages = Message.objects.filter(user__username=username)

        serializer = MessageListSerializer(messages, many=True)

        serializer_data = serializer.data

        custom_data = {'messages': serializer_data}

        return Response(custom_data)


class MessageSendAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSendSerializer

    def post(self,request,to_user ):
        serializer = MessageSendSerializer(data=request.data)
        serializer2 = MessageSendSerializer(data=request.data)
        user = User.objects.get(username=to_user)
        if serializer.is_valid() and serializer2.is_valid():
            serializer.save(from_user=request.user,user=user,conversation=request.user)
            serializer2.save(from_user=request.user, user=request.user, conversation=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

