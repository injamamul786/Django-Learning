from django.urls import path, register_converter
from . import views

urlpatterns = [
    path("user/", views.show_details, name='detail'),
]
