from django.urls import path
from landing_page import views

urlpatterns = [
    path('', views.landing_page, name='landing_page')
]
