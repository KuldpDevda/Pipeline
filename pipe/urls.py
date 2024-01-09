from django.urls import path
from .views import home,dashboard

urlpatterns = [
    path('home/',home, name='home'),
    path('dashboard/',dashboard, name='dashboard'),
]