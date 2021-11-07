from django.contrib.auth.decorators import login_required
from .models import User
from .serializers import *
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from django.db import router, transaction
from rest_framework import generics,status 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView


class AccountsView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SignUpView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get('username',None)
            if username:
                queryset = User.objects.filter(username=username)
                if queryset.exists():
                    return Response({'Error':'User Already Exists'},status=status.HTTP_404_NOT_FOUND)
                else:
                    print('huray')
                    serializer.save()
                    return Response({'Successful':'Successfully Signed Up'},status=status.HTTP_201_CREATED)
        else:
            return Response({'Error':'User Already Exists'},status=status.HTTP_406_NOT_ACCEPTABLE)


class SignInView(APIView):
    serializer_class = SignInUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username',None)
            password = serializer.validated_data.get('password',None)

            if username and password:
               
                try:
                    Account = User.objects.get(username=username)
                
                    if Account.check_password(password):
                        login(request,Account)
                        return redirect('chats')
                    return Response({'Message':'Invalid password'},status=status.HTTP_404_NOT_FOUND)
                except User.DoesNotExist:
                    return Response({'Message':'Invalid Login Credentials'},status=status.HTTP_404_NOT_FOUND)
            return Response({'Error':'if user and pp'},status=status.HTTP_202_ACCEPTED)
        else:
            return Response({'Error':'invalid data'},status=status.HTTP_406_NOT_ACCEPTABLE)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



def sign_in(request):
    return render(request, 'account/registration.html', )

@login_required
def sign_out(request): 
    logout(request)
    return redirect('sign_in')

def sign_up(request):
        return render(request, 'account/registration.html', )