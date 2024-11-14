# project/urls.py (головний файл)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('humsters.urls')),  # Підключаємо маршрути додатку
]
