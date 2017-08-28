from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


from boutique.models import Product
from reactions.api.serializers import InteractSerializer
from reactions.models import Reaction

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )


class InteractAPIView(CreateAPIView):
    serializer_class = InteractSerializer

    def post(self,request,prod_id ):
        serializer = InteractSerializer(data=request.data)
        prod = Product.objects.get(id=prod_id)
        if serializer.is_valid():
            try:
                reaction = Reaction.objects.get(user=request.user , product=prod)
                if reaction.reaction == serializer.validated_data['reaction']:
                    reaction.delete()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                	reaction.delete()
                	serializer.save(user=request.user,product=prod)
                	return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Reaction.DoesNotExist:
                serializer.save(user=request.user,product=prod)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)