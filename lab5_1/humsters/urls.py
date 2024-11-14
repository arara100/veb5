# app/urls.py (файл для додатку)

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HamsterViewSet

router = DefaultRouter()
router.register(r'hamsters', HamsterViewSet)  # Створюємо маршрут для хом'яків

urlpatterns = [
    path('', include(router.urls)),  # Додаємо маршрути з роутера
]
