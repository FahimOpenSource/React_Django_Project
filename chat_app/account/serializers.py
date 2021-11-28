from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import *
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        """create and return a new user"""
        account = Account(
            username= validated_data['username'],
            first_name= validated_data['first_name'],
            last_name= validated_data['last_name'],
            password= validated_data['password']
        )

        try:
            account.full_clean()
        except ValidationError as e:
            non_field_errors = e.message_dict[NON_FIELD_ERRORS]
            return non_field_errors
        account.save()

        return account
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.password = validated_data.get('password', instance.password)
        try:
            instance.full_clean()
        except ValidationError as e:
            non_field_errors = e.message_dict[NON_FIELD_ERRORS]
            return non_field_errors
        instance.save()

        return instance
 
