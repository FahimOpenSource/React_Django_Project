from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import *

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password':{'write_only': True}}
    def create(self, validated_data):
        """create and return a new user"""
        user = Account(
            username= validated_data['username'],
            first_name= validated_data['first_name'],
            last_name= validated_data['last_name']

        )

        user.set_password(validated_data['password'])
        user.save()
 
        return user

