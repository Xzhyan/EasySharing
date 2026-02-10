from django.urls import path
from . import views

urlpatterns = [
    path('main/<int:folder_id>', views.main_storage, name='main'),
    path('action/', views.actions, name='actions'),
    path('control/', views.control, name='control'),
]
