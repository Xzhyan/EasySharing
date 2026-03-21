from django.urls import path
from . import views

urlpatterns = [
    path('storage/', views.storage, name='storage'),
    path('main/<int:folder_id>', views.main_page, name='main'),
    path('action/<int:folder_id>', views.actions, name='actions'),
    path('control/', views.control, name='control'),
    path('message/', views.message, name='message')
]
