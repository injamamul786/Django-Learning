from django.urls import path, register_converter
from . import views


urlpatterns = [
    path("addshow/", views.addandshow, name='addshow'),
    path('update/', views.update, name='update'),
    path('delete/<int:id>/', views.delete_data, name='delete'),
    path('update/<int:id>/', views.update, name='update'), 
]