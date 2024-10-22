#!/usr/bin/env python3
__author__ = "DiegoGalvez"
#pages/urls.py
from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home'),
]