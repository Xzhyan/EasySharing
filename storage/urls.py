from django.urls import path
from . import views

urlpatterns = [
    path('storage/', views.storage, name='storage'),
    path('main/', views.main_page, name='main'),
    path('action/', views.actions, name='actions'),
    path('control/', views.control, name='control'),
]
