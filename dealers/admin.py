from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from Events.models import vehiclehystory
from .models import *
from import_export.admin import ImportExportModelAdmin
# # # User = get_user_model()

# # # class OrderAdmin(admin.ModelAdmin):
# # #     list_display = (
# # #          'vehicle_factory', 'vehicle_country', 'vehicle_series',
# # #         'vehicle_model_name', 'vehicle_color', 'vehicle_eu_type_approval',
# # #         'vehicle_body_type', 'vehicle_steering_power', 'vehicle_wheels',
# # #         'vehicle_screen', 'vehicle_lights', 'dealer', 'importer', 'orderer_email',
# # #         'orderer_name', 'orderer_phone', 'factory', 'status','vehicle_image','vehicle_subcategory'
# # #     )
# # #     list_filter = ('status', 'factory')
# # #     search_fields = ('vehicle__vin_code', 'dealer__username', 'orderer_email', 'orderer_name')



# # #     def vehicle_factory(self, obj):
# # #         return obj.vehicle.Factory_name.name if obj.vehicle and obj.vehicle.Factory_name else '-'
# # #     vehicle_factory.short_description = 'Vehicle Factory'

# # #     def vehicle_country(self, obj):
# # #         return obj.vehicle.country.name if obj.vehicle and obj.vehicle.country else '-'
# # #     vehicle_country.short_description = 'Vehicle Country'

# # #     def vehicle_series(self, obj):
# # #         return obj.vehicle.series.name if obj.vehicle and obj.vehicle.series else '-'
# # #     vehicle_series.short_description = 'Vehicle Series'

# # #     def vehicle_model_name(self, obj):
# # #         return obj.vehicle.model_name.name if obj.vehicle and obj.vehicle.model_name else '-'
# # #     vehicle_model_name.short_description = 'Vehicle Model Name'

# # #     def vehicle_color(self, obj):
# # #         return obj.vehicle.color.name if obj.vehicle and obj.vehicle.color else '-'
# # #     vehicle_color.short_description = 'Vehicle Color'

# # #     def vehicle_eu_type_approval(self, obj):
# # #         return obj.vehicle.eu_type_approval.name if obj.vehicle and obj.vehicle.eu_type_approval else '-'
# # #     vehicle_eu_type_approval.short_description = 'Vehicle EU Type Approval'

# # #     def vehicle_body_type(self, obj):
# # #         return obj.vehicle.body_type.name if obj.vehicle and obj.vehicle.body_type else '-'
# # #     vehicle_body_type.short_description = 'Vehicle Body Type'

# # #     def vehicle_steering_power(self, obj):
# # #         return obj.vehicle.steering_power.name if obj.vehicle and obj.vehicle.steering_power else '-'
# # #     vehicle_steering_power.short_description = 'Vehicle Steering Power'

# # #     def vehicle_wheels(self, obj):
# # #         return obj.vehicle.wheels.name if obj.vehicle and obj.vehicle.wheels else '-'
# # #     vehicle_wheels.short_description = 'Vehicle Wheels'

# # #     def vehicle_screen(self, obj):
# # #         return obj.vehicle.screen.name if obj.vehicle and obj.vehicle.screen else '-'
# # #     vehicle_screen.short_description = 'Vehicle Screen'

# # #     def vehicle_lights(self, obj):
# # #         return obj.vehicle.lights.name if obj.vehicle and obj.vehicle.lights else '-'
# # #     vehicle_lights.short_description = 'Vehicle Lights'
# # #     def vehicle_subcategory(self, obj):
# # #         return obj.vehicle.subcategory.name if obj.vehicle and obj.vehicle.subcategory else '-'
# # #     vehicle_subcategory.short_description = 'Vehicle Subcategory'

# # #     def vehicle_image(self, obj):
# # #         if obj.vehicle and obj.vehicle.image:
# # #             return format_html('<img src="{}" style="max-height: 100px;" />', obj.vehicle.image.url)
# # #         else:
# # #             return '-'
# # #     vehicle_image.short_description = 'Vehicle Image'



# # # # from django.contrib import admin
# # # # from .models import Order, FinalRegisteredVehicle






@admin.register(receivedvehicle)
class ReceivedVehicleAdmin(admin.ModelAdmin):
    list_display = ('status', 'get_sku_name', 'get_country', 'get_series', 'get_model_name', 'get_color',
        'get_eu_type',  'get_steering_power', 'get_wheels',
        'get_screen', 'get_lights', 'get_factory_name', 'get_CommunicationTerminal',
        'get_CargoCompartment')

    # search_fields = ('vin_code',  'order__vehicle__vin_code', 'order__dealer__username',
    #                  'order__orderer_email', 'order__orderer_name')

    # list_filter = ('manufacturing_date')
    exclude=('manufacturing_date','vehicle','name_received_product')
    def has_add_permission(self, request):
        return False
    def save_model(self, request, obj, form, change):
        # When saving the model, create a new historical record instead of updating
        # the existing instance
        if change:
            # This means the instance is being updated
            if obj.status == 'AR':
                new_status = form.cleaned_data['status']
                # The vehicle is registered and issued with a reg number
                history_instance = vehiclehystory.objects.create(
                    timestamp=timezone.now(),
                    description="The vehicle has been registered and issued with a reg number.",
                    historical_note="The vehicle is registered and issued with a reg number",
                    vehicle=obj.vehicle.vehicle,
                    owner_email=obj.vehicle.vehicle.orderer_email,
                    plate_number=obj.registration_number,
                    vin_code=obj.vin_code,
                )
                history_instance.save()
                print("data========================",obj.vehicle.vehicle),

                # Update the name_received_product field to indicate that the vehicle is issued with a reg number
                obj.name_received_product = "The vehicle is registered and issued with a reg number."
                super().save_model(request, obj, form, change)





                registered_vehicle_instance = RegisteredVehicle.objects.create(


                    sku=obj.vehicle.vehicle.sku.name if obj.vehicle.vehicle.sku else None,
                    manufacture=obj.vehicle.vehicle.Manufacturer.name if obj.vehicle.vehicle.Manufacturer else None,
                    country=obj.vehicle.vehicle.country.name if obj.vehicle.vehicle.country else None,
                    series=obj.vehicle.vehicle.series.name if obj.vehicle.vehicle.series else None,
                    model_name = str(obj.vehicle.vehicle.model_name) if obj.vehicle.vehicle.model_name else None,
                    vin_code=obj.vin_code,
                    vehicle_id=obj.vehicle.vehicle.id,
                    Plate_number=obj.registration_number,

                    factory_name=obj.vehicle.vehicle.Factory_name.name if obj.vehicle.vehicle.Factory_name else None,
                    color=obj.vehicle.vehicle.color.name if obj.vehicle.vehicle.color else None,
                    eu_type_approval=obj.vehicle.vehicle.eu_type.name if obj.vehicle.vehicle.eu_type else None,
                    steering_power=obj.vehicle.vehicle.steering_power.name if obj.vehicle.vehicle.steering_power else None,
                    wheels=obj.vehicle.vehicle.wheels.name if obj.vehicle.vehicle.wheels else None,
                    screen=obj.vehicle.vehicle.screen.name if obj.vehicle.vehicle.screen else None,
                    lights=obj.vehicle.vehicle.lights.name if obj.vehicle.vehicle.lights else None,
                    cargo_compartments=obj.vehicle.vehicle.cargo_compartment.name if obj.vehicle.vehicle.cargo_compartment else None,
                    communication_terminal=obj.vehicle.vehicle.communication_terminal.name if obj.vehicle.vehicle.communication_terminal else None,
                    date_of_manufacture=obj.manufacturing_date,
                    orderer=obj.vehicle.vehicle.orderer_name if obj.vehicle.vehicle.orderer_name else None,
                    orderer_phone=obj.vehicle.vehicle.orderer_phone if obj.vehicle.vehicle.orderer_phone else None,
                    orderer_email=obj.vehicle.vehicle.orderer_email if obj.vehicle.vehicle.orderer_email else None,
                    status='N',  # Set the status to 'RN' indicating that the vehicle is registered
                )
                registered_vehicle_instance.save()

                # Update the status field of the received vehicle to 'AR' after creating a record in RegisteredVehicle
                obj.status = new_status

        super().save_model(request, obj, form, change)
    def get_CommunicationTerminal(self, obj):
        return obj.vehicle.vehicle.communication_terminal.name if obj.vehicle.vehicle.communication_terminal else '-'
    get_CommunicationTerminal.short_description = 'CommunicationTerminal'

    def get_CargoCompartment(self, obj):
        return obj.vehicle.vehicle.cargo_compartment.name if obj.vehicle.vehicle.cargo_compartment else '-'
    get_CargoCompartment.short_description = 'CargoCompartment'

    def get_sku_name(self, obj):
        return obj.vehicle.vehicle.sku.name if obj.vehicle.vehicle.sku else '-'
    get_sku_name.short_description = 'Sku Name'

    def get_factory_name(self, obj):
        return obj.vehicle.vehicle.Factory_name.name if obj.vehicle.vehicle.Factory_name else '-'
    get_factory_name.short_description = 'Factory'

    def get_country(self, obj):
        return obj.vehicle.vehicle.country.name if obj.vehicle.vehicle.country else '-'
    get_country.short_description = 'Country'

    def get_series(self, obj):
        return obj.vehicle.vehicle.series.name if obj.vehicle.vehicle.series else '-'
    get_series.short_description = 'Series'

    def get_model_name(self, obj):
        return obj.vehicle.vehicle.model_name.name if obj.vehicle.vehicle.model_name else '-'
    get_model_name.short_description = 'Model Name'

    def get_color(self, obj):
        return obj.vehicle.vehicle.color.name if obj.vehicle.vehicle.color else '-'
    get_color.short_description = 'Color'

    def get_eu_type(self, obj):
        return obj.vehicle.vehicle.eu_type.name if obj.vehicle.vehicle.eu_type else '-'
    get_eu_type.short_description = 'EU Type '



    def get_steering_power(self, obj):
        return obj.vehicle.vehicle.steering_power.name if obj.vehicle.vehicle.steering_power else '-'
    get_steering_power.short_description = 'Steering Power'

    def get_wheels(self, obj):
        return obj.vehicle.vehicle.wheels.name if obj.vehicle.vehicle.wheels else '-'
    get_wheels.short_description = 'Wheels'

    def get_screen(self, obj):
        return obj.vehicle.vehicle.screen.name if obj.vehicle.vehicle.screen else '-'
    get_screen.short_description = 'Screen'

    def get_lights(self, obj):
        return obj.vehicle.vehicle.lights.name if obj.vehicle.vehicle.lights else '-'
    get_lights.short_description = 'Lights'

    # def get_subcategory(self, obj):
    #     return obj.vehicle.vehicle.subcategory.name if obj.vehicle.vehicle.subcategory else '-'
    # get_subcategory.short_description = 'Subcategory'

    # def vehicle_image(self, obj):
    #     if obj.vehicle.vehicle.image:
    #         return format_html('<img src="{}" style="max-height: 100px;" />',obj.vehicle.vehicle.image.url)
    #     else:
    #         return '-'
    # vehicle_image.short_description = 'Vehicle Image'


# # admin.site.register(Order, OrderAdmin)



# @admin.register(RegisteredVehicle)

class RegisteredVehicleAdmin(ImportExportModelAdmin):
    list_display = ('id',
        'status', 'sku', 'vin_code','Plate_number','country', 'series',
         'factory_name',  'orderer_phone', 'orderer_email'
    )

    # If you want to display the image in the list view, you can define a custom method like this:
    def display_image(self, obj):
        return obj.image.url if obj.image else ''

    display_image.short_description = 'Image'
    def has_add_permission(self, request):
        return False
    def save_model(self, request, obj, form, change):
        # When saving the model, create a new historical record instead of updating
        # the existing instance
        if change:
            # This means the instance is being updated
            if obj.status == 'y':
                new_status = form.cleaned_data['status']
                # The vehicle is registered and issued with a reg number
                history_instance = vehiclehystory.objects.create(
                    timestamp=timezone.now(),
                    description="The vehicle has been issued to the owner.",
                    historical_note="The vehicle has been issued to the owner.",
                    vehicle=obj.vehicle_id,
                    owner_email=obj.orderer_email,
                    # owner_email=obj.vehicle.vehicle.orderer_email,
                    plate_number=obj.Plate_number,
                    vin_code=obj.vin_code,


                )
                history_instance.save()

                # Update the name_received_product field to indicate that the vehicle is issued with a reg number

                # Update the status field of the received vehicle to 'AR' after creating a record in RegisteredVehicle
                obj.status = new_status

        super().save_model(request, obj, form, change)

    # ... Your other methods and configurations

admin.site.register(RegisteredVehicle, RegisteredVehicleAdmin)
