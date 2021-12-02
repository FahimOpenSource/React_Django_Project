from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import *

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'first_name', 'last_name','last_seen_time','last_seen_date']
        extra_kwargs = {'password':{'write_only': True}}

 
