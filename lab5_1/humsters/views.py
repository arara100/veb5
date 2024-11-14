# views.py
from rest_framework import viewsets
from .models import Humster
from .serializers import HumsterSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

class HamsterViewSet(viewsets.ModelViewSet):
    queryset = Humster.objects.all()
    serializer_class = HumsterSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['price']
    ordering_fields = ['price']
