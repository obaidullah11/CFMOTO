from django.contrib import admin
from .models import ApproveAdminVehicle
from importer.models import ConfirmVehicle
from django.utils.html import format_html

@admin.register(ApproveAdminVehicle)
class ApproveAdminVehicleAdmin(admin.ModelAdmin):
    list_display = (
        'vin_code',
        'get_manufacturer',
        'get_series',
        'get_factory_name',
        'get_model_name',
        'get_eu_type',
        'get_steering_power',
        'get_wheels',
        'get_color',
        'get_lights',
        'get_screen',
        'get_cargo_compartment',
        'get_communication_terminal',
        'get_country',
        'get_sku',
        
        'mileage',
        'approved_by',
        'status',
        'approval_date',
        'get_front_image',
        'get_back_image',

    )
    list_filter = ('approval_date', 'status')
    search_fields = ('vehicle_garage__Factory_name', 'vehicle_garage__series', 'vehicle_garage__model_name', 'approved_by__username')

    exclude = ('approved_by',)

    def save_model(self, request, obj, form, change):
        if obj.status == 'approved':
            obj.vehicle_garage.approved_by_admin = True
            obj.vehicle_garage.save()
            confirm_vehicle = ConfirmVehicle.objects.create(
                    vehicle_garage=obj.vehicle_garage,
                    # status='approved'
                )
            confirm_vehicle.save()
        self.message_user(request, f"vehicle has been approved by the admin and sent to the importer for verification")

        super().save_model(request, obj, form, change)

    

    def get_field_value(self, obj, field_name):
        vehicle_garage = obj.vehicle_garage
        return getattr(vehicle_garage, field_name)

    def get_manufacturer(self, obj):
        return self.get_field_value(obj, 'Manufacturer')

    def get_series(self, obj):
        return self.get_field_value(obj, 'series')

    def get_factory_name(self, obj):
        return self.get_field_value(obj, 'Factory_name')

    def get_model_name(self, obj):
        return self.get_field_value(obj, 'model_name')

    def get_eu_type(self, obj):
        return self.get_field_value(obj, 'eu_type')

    def get_steering_power(self, obj):
        return self.get_field_value(obj, 'steering_power')

    def get_wheels(self, obj):
        return self.get_field_value(obj, 'wheels')

    def get_color(self, obj):
        return self.get_field_value(obj, 'color')

    def get_lights(self, obj):
        return self.get_field_value(obj, 'lights')

    def get_screen(self, obj):
        return self.get_field_value(obj, 'screen')

    def get_cargo_compartment(self, obj):
        return self.get_field_value(obj, 'cargo_compartment')

    def get_communication_terminal(self, obj):
        return self.get_field_value(obj, 'communication_terminal')

    def get_country(self, obj):
        return self.get_field_value(obj, 'country')

    def get_sku(self, obj):
        return self.get_field_value(obj, 'sku')
    def get_front_image(self, obj):
        if obj.front_image:
            return format_html('<img src="{}" width="50" height="50" />', obj.front_image.url)
        return "No Front Image"
    
    get_front_image.short_description = 'Front rteteImage'

    def get_back_image(self, obj):
        if obj.back_image:
            return format_html('<img src="{}" width="50" height="50" />', obj.back_image.url)
        return "No Back Image"
    
    get_back_image.short_description = 'Backteeetr Image'

    # Define your get_field_value and get_* functions here...

    get_manufacturer.short_description = 'Manufacturer'
    get_series.short_description = 'Series'
    get_factory_name.short_description = 'Factory Name'
    get_model_name.short_description = 'Model Name'
    get_eu_type.short_description = 'EU Type'
    get_steering_power.short_description = 'Steering Power'
    get_wheels.short_description = 'Wheels'
    get_color.short_description = 'Color'
    get_lights.short_description = 'Lights'
    get_screen.short_description = 'Screen'
    get_cargo_compartment.short_description = 'Cargo Compartment'
    get_communication_terminal.short_description = 'Communication Terminal'
    get_country.short_description = 'Country'
    get_sku.short_description = 'SKU'

# admin.site.register(ApproveAdminVehicle, ApproveAdminVehicleAdmin)