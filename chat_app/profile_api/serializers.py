from django.core.exceptions import ValidationError
from rest_framework import serializers
from account.models import *
from .models import FriendRequest, Friend
from django.utils.translation import gettext_lazy as _


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'

    def validate(self, data):
        sent_to = data['sent_to']
        sent_by = data['sent_by']
        # makes sure you don't send a message to your self
        if sent_to == sent_by :
            raise ValidationError({
                'sent_to': ValidationError(_('may not equal to sent_to.'), code='invalid'),
                'sent_by': ValidationError(_('may not equal to sent_by.'), code='invalid'),
            })
        # makes sure that you either approve or decline a request
        elif data['declined'] and data['approved']:
            raise ValidationError({
                'approved': ValidationError(_('may not equal to approved.'), code='invalid'),
                'declined': ValidationError(_('may not equal to declined.'), code='invalid')
            })
        # makes sure that you don't send a requests if there is one not yet approved or declined
        else:
            if not data['declined'] and not data['approved']:
                request = FriendRequest.objects.filter(sent_by=sent_by, sent_to=sent_to)
                if request.exists():
                    if not request[0].approved and not request[0].declined:
                        raise ValidationError({
                            'request':_('request still pending')
                            })
        return data

    def update(self, instance, validated_data):
        instance.declined = validated_data.get('declined',instance.declined)
        instance.approved = validated_data.get('approved',instance.approved)
        instance.save()

        # checks to see if a request was approved 
        if instance.approved:
            # makes sure you don't have the person as a friend already
            friend = Friend.objects.filter(approved_request=instance)
            if friend.exists():
                return instance
            else:
                # creates a two friends each representing an account in pairs
                my_new_friend = Friend(account=instance.sent_to, friend_account=instance.sent_by, approved_request=instance)
                his_new_friend = Friend(account=instance.sent_by, friend_account=instance.sent_to, approved_request=instance)
                my_new_friend.save()
                his_new_friend.save()
                return instance
                
        return instance

class FilteredListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(chat=True)
        return super(FilteredListSerializer, self).to_representation(data)

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = FilteredListSerializer
        model = Friend
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    received = FriendRequestSerializer(many=True, read_only=True)
    sent = FriendRequestSerializer(many=True, read_only=True)
    class Meta:
        model = Account
        fields = ['id', 'username', 'first_name', 'last_name','active','date_joined','received','sent','friends']
        depth = 1
    



