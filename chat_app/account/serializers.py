from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'first_name', 'last_name','last_seen_time','last_seen_date']
        extra_kwargs = {'password':{'write_only': True}}

class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=15)
    password = serializers.CharField(required=True, max_length=15)