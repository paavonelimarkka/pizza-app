from django.shortcuts import render
from django.contrib.auth.models import User

def landing_page(request):
    return render(request, 'landing_page.html', {})