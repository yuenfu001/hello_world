from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.

def home(request):
    return HttpResponse("<h3>This is a Home Page</h3>")