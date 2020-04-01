from django.shortcuts import render, HttpResponse
from django.template.context import RequestContext

# Create your views here.

def index(requests):
    return HttpResponse('Hello')

def render_login(requests):
    return render(requests, 'login.html')

def login():
    pass