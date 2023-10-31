from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(vehiclehystory)
class VehicleHystoryAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'description', 'historical_note', 'vehicle_sku','owner_email','vin_code','plate_number')
    list_filter = ('vehicle__sku', 'owner_email', 'vin_code', 'plate_number') 
    def vehicle_sku(self, obj):
        return obj.vehicle.sku if obj.vehicle else '-'