from django.contrib.auth.decorators import login_required
from .models import User
from .serializers import *
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import router, transaction
from rest_framework import generics,status 
from rest_framework.views import APIView
from rest_framework.response import Response

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
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('chats')
                else:
                    pass

def sign_in(request):
    return render(request, 'account/registration.html', )

@login_required
def sign_out(request): 
    logout(request)
    return redirect('sign_in')

def sign_up(request):
        return render(request, 'account/signup.html', )

