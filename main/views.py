from django.shortcuts import render
from django.contrib.auth.models import User

def main(request):
    return render(request, 'main.html', {})