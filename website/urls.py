from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='home'),
]