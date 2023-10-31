from rest_framework import serializers
from .models import *





class RegisteredVehicleSerializer(serializers.ModelSerializer):
    # received_vehicle = ReceivedVehicleSerializer()  # Include fields from ReceivedVehicle model

    class Meta:
        model = RegisteredVehicle
        fields = '__all__'

         # Include all fields from RegisteredVehicle model
