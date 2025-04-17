from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms-and-conditions'),
    path('', include('users.urls')),  # Inclusion des URLs de l'application users
]
