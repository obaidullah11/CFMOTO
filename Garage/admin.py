from django.contrib import admin
from .models import VehicleGarage
from django.contrib import admin, messages
from CFMOTO_Admin.models import ApproveAdminVehicle

@admin.register(VehicleGarage)
class VehicleGarageAdmin(admin.ModelAdmin):
    list_display = ('Manufacturer', 'series', 'Factory_name', 'model_name', 'eu_type', 'steering_power', 'wheels', 'color', 'lights', 'screen', 'cargo_compartment', 'communication_terminal', 'country', 'sku', 'user_email', 'user_name', 'user_phone', 'approved_by_admin')
    list_filter = ('approved_by_admin',)  # Add a filter for approved_by_admin field
    search_fields = ('Manufacturer', 'series', 'Factory_name', 'model_name', 'user_email')  # Add fields for searching

    def get_queryset(self, request):
        # Override the queryset to exclude entries where approved_by_admin is False
        queryset = super().get_queryset(request)
        return queryset.filter(approved_by_admin=True)
    def save_model(self, request, obj, form, change):
        if not change:  # Check if it's a new object being created
        # Save the current VehicleGarage instance
         super().save_model(request, obj, form, change)

        if not change and not obj.approved_by_admin:
        # Create a new ApproveAdminVehicle instance
            ApproveAdminVehicle.objects.create(vehicle_garage=obj, mileage=0,approved_by=request.user)

            # Display a success message
            messages.success(request, 'The vehicle has been added to the garage. The administrator is requested to approve the vehicle. Once approved, it will be displayed here.')
        else:
        # For existing objects, save as usual without triggering additional actions
         super().save_model(request, obj, form, change)