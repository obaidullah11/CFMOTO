# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.utils.html import format_html
# from .models import *

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






# @admin.register(receivedvehicle)
# class ReceivedVehicleAdmin(admin.ModelAdmin):
#     list_display = ('status','vin_code', 'vehicle_country', 'vehicle_series',
#                     'vehicle_model_name', 'vehicle_color', 'vehicle_eu_type_approval',
#                     'vehicle_body_type', 'vehicle_steering_power', 'vehicle_wheels',
#                     'vehicle_screen', 'vehicle_lights', 'order_dealer', 'order_importer', 'order_orderer_email',
#                     'order_orderer_name', 'order_orderer_phone', 'order_factory', 'order_status','vehicle_subcategory', 'vehicle_image','name_received_product','manufacturing_date')

#     # search_fields = ('vin_code',  'order__vehicle__vin_code', 'order__dealer__username',
#     #                  'order__orderer_email', 'order__orderer_name')

#     # list_filter = ('manufacturing_date')
#     exclude=('manufacturing_date','registration_number')

#     def vin_code(self, obj):
#         return obj.vin_code

#     def order_dealer(self, obj):
#         return obj.order.dealer if obj.order else '-'

#     def order_importer(self, obj):
#         return obj.order.importer if obj.order else '-'

#     def order_orderer_email(self, obj):
#         return obj.order.orderer_email if obj.order else '-'

#     def order_orderer_name(self, obj):
#         return obj.order.orderer_name if obj.order else '-'

#     def order_orderer_phone(self, obj):
#         return obj.order.orderer_phone if obj.order else '-'

#     def order_factory(self, obj):
#         return obj.order.factory if obj.order else '-'

#     def order_status(self, obj):
#         return obj.order.get_status_display() if obj.order else '-'

#     def vehicle_country(self, obj):
#         return obj.order.vehicle.country.name if obj.order and obj.order.vehicle else '-'

#     def vehicle_series(self, obj):
#         return obj.order.vehicle.series.name if obj.order and obj.order.vehicle and obj.order.vehicle.series else '-'

#     def vehicle_model_name(self, obj):
#         return obj.order.vehicle.model_name.name if obj.order and obj.order.vehicle and obj.order.vehicle.model_name else '-'

#     def vehicle_color(self, obj):
#         return obj.order.vehicle.color.name if obj.order and obj.order.vehicle and obj.order.vehicle.color else '-'

#     def vehicle_eu_type_approval(self, obj):
#         return obj.order.vehicle.eu_type_approval.name if obj.order and obj.order.vehicle and obj.order.vehicle.eu_type_approval else '-'

#     def vehicle_body_type(self, obj):
#         return obj.order.vehicle.body_type.name if obj.order and obj.order.vehicle and obj.order.vehicle.body_type else '-'

#     def vehicle_steering_power(self, obj):
#         return obj.order.vehicle.steering_power.name if obj.order and obj.order.vehicle and obj.order.vehicle.steering_power else '-'

#     def vehicle_wheels(self, obj):
#         return obj.order.vehicle.wheels.name if obj.order and obj.order.vehicle and obj.order.vehicle.wheels else '-'

#     def vehicle_screen(self, obj):
#         return obj.order.vehicle.screen.name if obj.order and obj.order.vehicle and obj.order.vehicle.screen else '-'

#     def vehicle_lights(self, obj):
#         return obj.order.vehicle.lights.name if obj.order and obj.order.vehicle and obj.order.vehicle.lights else '-'
#     def vehicle_subcategory(self, obj):
#         return obj.order.vehicle.subcategory.name if obj.order and obj.order.vehicle and obj.order.vehicle.subcategory else '-'
#     vehicle_subcategory.short_description = 'Vehicle Subcategory'

#     def vehicle_image(self, obj):
#         if obj.order and obj.order.vehicle and obj.order.vehicle.image:
#             return format_html('<img src="{}" style="max-height: 100px;" />', obj.order.vehicle.image.url)
#         else:
#             return '-'
#     vehicle_image.short_description = 'Vehicle Image'

#     vin_code.short_description = 'VIN Code'
#     order_dealer.short_description = 'Dealer'
#     order_importer.short_description = 'Importer'
#     order_orderer_email.short_description = 'Orderer Email'
#     order_orderer_name.short_description = 'Orderer Name'
#     order_orderer_phone.short_description = 'Orderer Phone'
#     order_factory.short_description = 'Factory'
#     order_status.short_description = 'Status'
#     vehicle_country.short_description = 'Country'
#     vehicle_series.short_description = 'Series'
#     vehicle_model_name.short_description = 'Model Name'
#     vehicle_color.short_description = 'Color'
#     vehicle_eu_type_approval.short_description = 'EU Type Approval'
#     vehicle_body_type.short_description = 'Body Type'
#     vehicle_steering_power.short_description = 'Steering Power'
#     vehicle_wheels.short_description = 'Wheels'
#     vehicle_screen.short_description = 'Screen'
#     vehicle_lights.short_description = 'Lights'



# # admin.site.register(Order, OrderAdmin)