from django.contrib import admin,messages
from .models import newOrder
from django.utils.html import format_html
from django.utils import timezone
from Events.models import vehiclehystory
from importer.models import DeliveredVehicle
from django.core.exceptions import ObjectDoesNotExist

@admin.register(newOrder)
class newOrderAdmin(admin.ModelAdmin):
    list_display = ('dealer_username', 'status','get_sku_name', 'get_country', 'get_series', 'get_model_name', 'get_color', 'get_eu_type_approval',  'get_steering_power', 'get_wheels', 'get_screen', 'get_lights','get_factory_name','get_CommunicationTerminal','get_CargoCompartment', )
    list_filter = ('status',)
    search_fields = ('vehicle__sku__name', 'dealer__username')  # Replace with relevant fields for searching
    exclude=('vehicle','dealer')
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        # Allow changing (updating) the status field for existing objects
        if obj is not None and request.method in ['GET', 'POST']:
            return True
        return super().has_change_permission(request, obj)

    def save_model(self, request, obj, form, change):
        if change and 'status' in form.changed_data and form.cleaned_data['status'] == 'S':
            # Create a historical record if the status is changed to 'P'
            history_instance = vehiclehystory.objects.create(
                timestamp=timezone.now(),
                description="The vehicle is out of production.",
                historical_note="The vehicle is out of production.",
                vehicle=obj.vehicle,
                owner_email=obj.vehicle.orderer_email,
            )

            # Save the historical record instance to add it to the database
            history_instance.save()

            # Create a DeliveredVehicle instance when the status is changed to 'S'
            try:
                last_delivered_vehicle = DeliveredVehicle.objects.latest('vehicle_system_id')
                last_vehicle_system_id = last_delivered_vehicle.vehicle_system_id
                last_system_id_number = int(last_vehicle_system_id.split('-')[1])
                new_system_id_number = last_system_id_number + 1
            except ObjectDoesNotExist:
                # No DeliveredVehicle exists yet, so start with a default value
                new_system_id_number = 1

            new_vehicle_system_id = f"1000-{new_system_id_number:04d}"  # Format to '1000-XXXX'

            delivered_vehicle_instance = DeliveredVehicle.objects.create(
                vehicle_system_id=new_vehicle_system_id,
                vehicle=obj.vehicle,
                status='OW',  # Assuming the status should be 'OW' (Arrived at warehouse)
            )

            # Save the DeliveredVehicle instance
            delivered_vehicle_instance.save()

            # Show a success message to inform the user that the product has been shipped
            messages.success(request, "The product has been shipped to the warehouse.")

        # Save the current newOrder instance
        super().save_model(request, obj, form, change)
    def get_sku_name(self, obj):
        return obj.vehicle.sku.name if obj.vehicle and obj.vehicle.sku else '-'
    get_sku_name.short_description = 'Sku Name'

    def get_country(self, obj):
        return obj.vehicle.country.name if obj.vehicle and obj.vehicle.country else '-'
    get_country.short_description = 'Country'

    def get_series(self, obj):
        return obj.vehicle.series.name if obj.vehicle and obj.vehicle.series else '-'
    get_series.short_description = 'Series'

    def get_model_name(self, obj):
        return obj.vehicle.model_name.name if obj.vehicle and obj.vehicle.model_name else '-'
    get_model_name.short_description = 'Model Name'

    def get_color(self, obj):
        return obj.vehicle.color.name if obj.vehicle and obj.vehicle.color else '-'
    get_color.short_description = 'Color'

    def get_eu_type_approval(self, obj):
        return obj.vehicle.eu_type.name if obj.vehicle and obj.vehicle.eu_type else '-'
    get_eu_type_approval.short_description = 'EU Type Approval'



    def get_steering_power(self, obj):
        return obj.vehicle.steering_power.name if obj.vehicle and obj.vehicle.steering_power else '-'
    get_steering_power.short_description = 'Steering Power'

    def get_wheels(self, obj):
        return obj.vehicle.wheels.name if obj.vehicle and obj.vehicle.wheels else '-'
    get_wheels.short_description = 'Wheels'

    def get_screen(self, obj):
        return obj.vehicle.screen.name if obj.vehicle and obj.vehicle.screen else '-'
    get_screen.short_description = 'Screen'

    def get_lights(self, obj):
        return obj.vehicle.lights.name if obj.vehicle and obj.vehicle.lights else '-'
    get_lights.short_description = 'Lights'

    def get_factory_name(self, obj):
        return obj.vehicle.Factory_name.name if obj.vehicle and obj.vehicle.Factory_name else '-'
    get_factory_name.short_description = 'Factory Name'
    def dealer_username(self, obj):
        return obj.dealer.name if obj.dealer else '-'
    dealer_username.short_description = 'Dealer Username'

    def get_CommunicationTerminal(self, obj):
        return obj.vehicle.communication_terminal.name if obj.vehicle and obj.vehicle.communication_terminal else '-'
    get_CommunicationTerminal.short_description = 'Communication Terminal'

    def get_CargoCompartment(self, obj):
        return obj.vehicle.cargo_compartment.name if obj.vehicle and obj.vehicle.cargo_compartment else '-'
    get_CargoCompartment.short_description = 'Cargo Compartment'


