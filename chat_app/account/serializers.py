from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import *
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'first_name', 'last_name']
        # to make sure that the password can't be seen on the front end
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        """create and return a new user"""
        account = Account(
            username= validated_data['username'],
            first_name= validated_data['first_name'],
            last_name= validated_data['last_name'],
            password= validated_data['password']
        )

        # makes sure that the password is hashed when an account is created we run a full clean 
        account.full_clean()
        account.save()

        return account
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)

        # makes sure that the password is hashed when an account's `password` is updated we run a full clean 
        instance.full_clean()
        instance.save()

        return instance
 
