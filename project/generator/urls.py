from django.contrib import admin
from django.urls import path, include
from .views import main_view

app_name = 'generator'


urlpatterns = [
    path('', main_view)
]