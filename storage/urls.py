from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main_storage, name='main'),
    path('action/', views.actions, name='actions'),
]
