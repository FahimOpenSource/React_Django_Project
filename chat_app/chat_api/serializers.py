from .models import *
from rest_framework import serializers
from account.models import *

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

# make sure an account cant send a message to a friend model with its account

class InboxSerializer(serializers.ModelSerializer):
    sent = MessageSerializer(many=True, read_only=True)
    received = MessageSerializer(many=True, read_only=True)
    class Meta:
        model = Inbox
        fields = '__all__'


class ChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'first_name', 'last_name','active','date_joined','chats']
        depth = 1
