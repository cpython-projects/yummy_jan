from django.urls import path
from .views import manager_main

app_name = 'manager'

urlpatterns = [
    path('', manager_main, name='manager_main'),
]