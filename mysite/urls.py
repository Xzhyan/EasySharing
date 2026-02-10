from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('__reload__/', include('django_browser_reload.urls')),
    path('admin/', admin.site.urls),

    # Rotas do sistema
    path('', include('users.urls')),
    path('', include('storage.urls')),
]
