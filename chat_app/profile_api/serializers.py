from rest_framework import serializers
from account.models import *
from .models import *


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'


class FriendSerializer(serializers.ModelSerializer):
    class Meta:

        model = Friend
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.declined = validated_data.get('declined',instance.declined)
        instance.approved = validated_data.get('approved',instance.approved)
        instance.sent_to = validated_data.get('sent_to',instance.sent_to)
        instance.sent_by = validated_data.get('sent_by',instance.sent_by)
        instance.save()
    
        return instance

class ProfileSerializer(serializers.ModelSerializer):
    friends = FriendSerializer(many=True, read_only=True)
    received = FriendRequestSerializer(many=True, read_only=True)
    sent = FriendRequestSerializer(many=True, read_only=True)
    class Meta:
        model = Account
        fields = ['id', 'username', 'first_name', 'last_name','active','date_joined','received','sent','friends']

    



