# serializers.py
from rest_framework import serializers
from .models import vehiclehystory

class VehicleHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = vehiclehystory
        fields = '__all__'
