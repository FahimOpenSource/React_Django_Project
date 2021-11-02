from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signin(request):
    return render(request, 'account/signin.html', )
