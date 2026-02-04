from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='user-login'),
    path('register/', views.user_register, name='user-register'),
    path('logout/', views.user_logout, name='user-logout'),
    path('user/edit/<int:pk>', views.user_edit, name='user-edit'),
    path('user/delete/', views.user_delete, name='user-delete')
]
