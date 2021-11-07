from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password':{'write_only': True}}
    def create(self, validated_data):
        """create and return a new user"""
        user = User(
            username= validated_data['username'],
            first_name= validated_data['first_name'],
            last_name= validated_data['last_name']

        )

        user.set_password(validated_data['password'])
        user.save()
 
        return user

class SignInUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=190)
    password = serializers.CharField(max_length=128, write_only=True)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token