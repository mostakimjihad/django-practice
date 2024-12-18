from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the home page.")

def login(request):
    return HttpResponse("You're at the login page.")