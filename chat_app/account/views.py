from django.contrib.auth.decorators import login_required
from django.http import response
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
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SignUpView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get('username',None)
            password = serializer.validated_data.get('password',None)
            if username:
                queryset = User.objects.filter(username=username)

                if queryset.exists():
                    return Response({'Message':'Username Already Exists'},status=status.HTTP_406_NOT_ACCEPTABLE)
                else:
                    serializer.save()
                    response = redirect('chats')
                    return response
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
                    user = User.objects.get(username=username)
                
                    if user.check_password(password):
                        return redirect('chats')

                    return Response({'Message':'Invalid password'},status=status.HTTP_404_NOT_FOUND)
                except User.DoesNotExist:
                    return Response({'Message':'User does not exist'},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'Error':'invalid data'},status=status.HTTP_406_NOT_ACCEPTABLE)


# def sign_in(username, password):



@login_required
def sign_out(request): 
    logout(request)
    return redirect('sign_in')

# def sign_up(request):
       

def register(request):
    return render(request, 'account/registration.html', )



# def set_access_cookie(response,user):
#     tokens = get_tokens_for_user(user)
#     access_token = tokens['access']
#     refresh_token = tokens['refresh']   
#     response.set_cookie("access_token",value=access_token,max_age=None)
#     response.set_cookie("refresh_token",value=refresh_token,max_age=None)
#     return response
  
