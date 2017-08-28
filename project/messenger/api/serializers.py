from rest_framework.serializers import ModelSerializer, SerializerMethodField

from project.messenger.models import Message


class MessageListSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'message', 'date', 'is_read', 'user')


class MessageSendSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['message','product']

        # class ProductCreateUpdateSerializer(ModelSerializer):
        #     class Meta:
        #         model = Product
        #         fields = [
        #             # 'id',
        #             'name',
        #             'description',
        #             'price',
        #             'quantite',
        #             'is_active',
        #             'origin',
        #             'likes',
        #             'principal_picture',
        #             'category',
        #
        #         ]