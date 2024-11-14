from rest_framework import serializers
from .models import Humster

class HumsterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Humster
        fields = '__all__'
