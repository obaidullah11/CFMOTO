from django.contrib import admin
from .models import vehiclehystory
from django.utils.dateformat import DateFormat

@admin.register(vehiclehystory)
class VehicleHystoryAdmin(admin.ModelAdmin):
    list_display = ('formatted_timestamp', 'description', 'historical_note', 'vehicle_sku','owner_email','vin_code','plate_number')
    list_filter = ('vehicle__sku', 'owner_email', 'vin_code', 'plate_number') 

    def vehicle_sku(self, obj):
        return obj.vehicle.sku if obj.vehicle else '-'

    def formatted_timestamp(self, obj):
        return DateFormat(obj.timestamp).format('d/m/Y H:i')
    formatted_timestamp.admin_order_field = 'timestamp' # Allows column order sorting
    formatted_timestamp.short_description = 'Timestamp'  # Renames column head

