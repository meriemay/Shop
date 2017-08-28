from django.db.migrations import serializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from boutique.models import Product
from reactions.models import Reaction




class InteractSerializer(ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['reaction']