from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("instagram/",views.app1)
    
]
