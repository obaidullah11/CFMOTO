from django.contrib import admin
from django.utils.html import format_html
from .models import DeliveredVehicle,ConfirmVehicle
from django.utils import timezone
from Events.models import vehiclehystory
from dealers.models import receivedvehicle

@admin.register(DeliveredVehicle)
class DeliveredVehicleAdmin(admin.ModelAdmin):
    list_display = (
        'status', 'vehicle_system_id',
        'get_sku_name', 'get_country', 'get_series', 'get_model_name', 'get_color', 
        'get_eu_type', 'get_steering_power', 'get_wheels', 
        'get_screen', 'get_lights', 'get_factory_name', 'get_CommunicationTerminal', 
        'get_CargoCompartment'
    )
    list_filter = ('status',)
    search_fields = ('vehicle_system_id', 'vehicle__make', 'vehicle__model')
    exclude = ('vehicle_system_id', 'vehicle')

    def has_add_permission(self, request):
        return False

    def save_model(self, request, obj, form, change):
        if 'status' in form.changed_data:
            new_status = form.cleaned_data['status']
            if new_status == 'AW':
                # Create a historical record when the status is changed to 'AW'
                history_instance = vehiclehystory.objects.create(
                    timestamp=timezone.now(),
                    description="The vehicle arrived at the MOTOHOBI warehouse.",
                    historical_note="The vehicle arrived at the MOTOHOBI warehouse.",
                    vehicle=obj.vehicle,
                    owner_email=obj.vehicle.orderer_email,
                )
                history_instance.save()
            elif new_status == 'TD':
                # Create a historical record when the status is changed to 'TD'
                history_instance = vehiclehystory.objects.create(
                    timestamp=timezone.now(),
                    description="The vehicle has been transferred to the dealer.",
                    historical_note="The vehicle has been transferred to the dealer.",
                    vehicle=obj.vehicle,
                    owner_email=obj.vehicle.orderer_email,
                )
                history_instance.save()

                # Create a record in ReceivedVehicle model
                received_vehicle_instance = receivedvehicle.objects.create(
                    # manufacturing_date=obj.manufacturing_date,
                    # vin_code=obj.vin_code,
                    vehicle=obj,
                    status='PN',
                    name_received_product=request.user.get_full_name(),
                )
                received_vehicle_instance.save()

        # Set the status to the new_status when saving the model
        obj.status = new_status

        # Save the current DeliveredVehicle instance
        super().save_model(request, obj, form, change)



    def get_CommunicationTerminal(self, obj):
        return obj.vehicle.communication_terminal.name if obj.vehicle.communication_terminal else '-'
    get_CommunicationTerminal.short_description = 'CommunicationTerminal'

    def get_CargoCompartment(self, obj):
        return obj.vehicle.cargo_compartment.name if obj.vehicle.cargo_compartment else '-'
    get_CargoCompartment.short_description = 'CargoCompartment'

    def get_sku_name(self, obj):
        return obj.vehicle.sku.name if obj.vehicle.sku else '-'
    get_sku_name.short_description = 'Sku Name'

    def get_factory_name(self, obj):
        return obj.vehicle.Factory_name.name if obj.vehicle.Factory_name else '-'
    get_factory_name.short_description = 'Factory'

    def get_country(self, obj):
        return obj.vehicle.country.name if obj.vehicle.country else '-'
    get_country.short_description = 'Country'

    def get_series(self, obj):
        return obj.vehicle.series.name if obj.vehicle.series else '-'
    get_series.short_description = 'Series'

    def get_model_name(self, obj):
        return obj.vehicle.model_name.name if obj.vehicle.model_name else '-'
    get_model_name.short_description = 'Model Name'

    def get_color(self, obj):
        return obj.vehicle.color.name if obj.vehicle.color else '-'
    get_color.short_description = 'Color'

    def get_eu_type(self, obj):
        return obj.vehicle.eu_type.name if obj.vehicle.eu_type else '-'
    get_eu_type.short_description = 'EU Type '

    

    def get_steering_power(self, obj):
        return obj.vehicle.steering_power.name if obj.vehicle.steering_power else '-'
    get_steering_power.short_description = 'Steering Power'

    def get_wheels(self, obj):
        return obj.vehicle.wheels.name if obj.vehicle.wheels else '-'
    get_wheels.short_description = 'Wheels'

    def get_screen(self, obj):
        return obj.vehicle.screen.name if obj.vehicle.screen else '-'
    get_screen.short_description = 'Screen'

    def get_lights(self, obj):
        return obj.vehicle.lights.name if obj.vehicle.lights else '-'
    get_lights.short_description = 'Lights'

    # def get_subcategory(self, obj):
    #     return obj.vehicle.subcategory.name if obj.vehicle.subcategory else '-'
    # get_subcategory.short_description = 'Subcategory'

    # def vehicle_image(self, obj):
    #     if obj.vehicle.image:
    #         return format_html('<img src="{}" style="max-height: 100px;" />', obj.vehicle.image.url)
    #     else:
    #         return '-'
    # vehicle_image.short_description = 'Vehicle Image'

@admin.register(ConfirmVehicle)
class ConfirmVehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_garage', 'status', 'confirmation_date',
                    'factory_name', 'series', 'model_name',
                    'eu_type', 'steering_power', 'wheels',
                    'color', 'lights', 'screen', 'cargo_compartment',
                    'communication_terminal', 'country', 'sku',
                    'user_email', 'user_name', 'user_phone',
                    'approved_by_admin')
    list_filter = ('confirmation_date', 'status')
    search_fields = ('vehicle_garage__Factory_name', 'vehicle_garage__series', 'vehicle_garage__model_name')

    def factory_name(self, obj):
        return obj.vehicle_garage.Factory_name

    def series(self, obj):
        return obj.vehicle_garage.series

    def model_name(self, obj):
        return obj.vehicle_garage.model_name

    def eu_type(self, obj):
        return obj.vehicle_garage.eu_type

    def steering_power(self, obj):
        return obj.vehicle_garage.steering_power

    def wheels(self, obj):
        return obj.vehicle_garage.wheels

    def color(self, obj):
        return obj.vehicle_garage.color

    def lights(self, obj):
        return obj.vehicle_garage.lights

    def screen(self, obj):
        return obj.vehicle_garage.screen

    def cargo_compartment(self, obj):
        return obj.vehicle_garage.cargo_compartment

    def communication_terminal(self, obj):
        return obj.vehicle_garage.communication_terminal

    def country(self, obj):
        return obj.vehicle_garage.country

    def sku(self, obj):
        return obj.vehicle_garage.sku

    def user_email(self, obj):
        return obj.vehicle_garage.user_email

    def user_name(self, obj):
        return obj.vehicle_garage.user_name

    def user_phone(self, obj):
        return obj.vehicle_garage.user_phone

    def approved_by_admin(self, obj):
        return obj.vehicle_garage.approved_by_admin

    factory_name.short_description = 'Factory Name'
    # Define similar methods for other fields