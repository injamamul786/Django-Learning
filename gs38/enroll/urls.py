from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.showformdata, name="registration"),
    path('success/', views.success),
]