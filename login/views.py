from django.shortcuts import render
from django.contrib.auth.models import User

def login(request):
    return render(request, 'login.html', {})