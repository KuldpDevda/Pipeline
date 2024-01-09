from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the CICD Pipeline app!")

def dashboard(request):
    return HttpResponse('Hello from the Kuldeep Devda Website!')