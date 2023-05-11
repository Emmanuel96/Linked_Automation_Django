from django.contrib import admin
from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('apply/', views.apply, name='apply'),
    path('connect/', views.connect, name="connect")
]