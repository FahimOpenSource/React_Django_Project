from .models import *
from rest_framework import serializers
from account.models import *
from profile_api.serializers import FriendSerializer

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

    def validate(self, data):
        # makes sure you can't send a message to yourself 
        if data['sent_to'] == data['sent_by'] :
            raise ValidationError({
                'sent_to': ValidationError(_('may not equal to sent_to.'), code='invalid'),
                'sent_by': ValidationError(_('may not equal to sent_by.'), code='invalid'),
            })
        # makes sure you either have a text or a file(response) you want to send or both
        elif not self.text or self.response:
            raise ValidationError({
                'required': ValidationError(_('alteast text or response is required.'))
            })

        return data

    def create(self, validated_data):
        # creates a message from validated data
        message = Message(
            forwaded_message = validated_data['forwaded_message'],
            text = validated_data['text'],
            sent_to = validated_data['sent_to'],
            sent_by = validated_data['sent_by'],
            response = validated_data['response'],
            
        )

        message.save()

        # gets the id of the friend to wich the message is sent
        sent_to_id = message.sent_to
        friend = Friend.objects.get(pk=sent_to_id)
        # checks to see if the friend already has an inbox
        if not friend.chat:
            # if not creates the inbox
            friend.chat = True
            friend.save(update_fields=['chat'])
            return message

        return message


class InboxSerializer(serializers.ModelSerializer):
    sent = MessageSerializer(many=True, read_only=True)
    received = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Friend
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.chat = validated_data.get('chat',instance.chat)
        instance.blocked = validated_data.get('blocked',instance.blocked)
        instance.save()
        return instance

class ChatsSerializer(serializers.ModelSerializer):
    chats = FriendSerializer(many=True, read_only=True, source='friends')
    class Meta:
        model = Account
        fields = ['id', 'username', 'first_name', 'last_name','active','date_joined','chats']
        
