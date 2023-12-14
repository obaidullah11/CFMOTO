from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
from import_export import resources, fields
from django.contrib import admin, messages
from django.utils import timezone
from Events.models import vehiclehystory
from factory.models import newOrder
from import_export.widgets import ForeignKeyWidget

class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1

from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Category, Subcategory, SKU

# Your existing resources and admin classes for SteeringPower, Wheels, CommunicationTerminal, Screen, Factory, and Lights
# ...

class CategoryResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Category')  # Add other fields if needed

    class Meta:
        model = Category
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'description',)  # Add more fields if needed
        import_id_fields = ['name']  # Use 'name' as the identifier for deduplication

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)

        # Get the objects from the result of the import
        new_categories = resource.get_queryset()
        print("--------------", new_categories)

        # Save each imported object to the database
        for category in new_categories:
            print("--------------", category)
            category.save()

        return result

    list_display = ('name', 'description')  # Add more fields if needed

class SubcategoryResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Subcategory')  # Add other fields if needed

    class Meta:
        model = Subcategory
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'parent',)  # Add more fields if needed
        import_id_fields = ['name']  # Use 'name' as the identifier for deduplication

@admin.register(Subcategory)
class SubcategoryAdmin(ImportExportModelAdmin):
    resource_class = SubcategoryResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)

        # Get the objects from the result of the import
        new_subcategories = resource.get_queryset()
        print("--------------", new_subcategories)

        # Save each imported object to the database
        for subcategory in new_subcategories:
            print("--------------", subcategory)
            subcategory.save()

        return result

    list_display = ('name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name', 'parent__name')

class SKUResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Sku')
    # category = fields.Field(column_name='Category', attribute='get_category_name')
    category = fields.Field(
        column_name='Category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'name'))

    def get_category_name(self, instance):
        cat = Category.objects.filter(name=instance.category).first()
        if cat:
            return cat
        else:
            cat = Category.objects.create(name=instance.category)
        return cat.id
        # print("i am in get category nmame ",instance)
        # if instance.category:
        #     return instance.category.name
        # return ''

    class Meta:
        model = SKU
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'description','category')  # Add more fields if needed
        import_id_fields = ['name']  # Use 'name' as the identifier for deduplication

@admin.register(SKU)
class SKUAdmin(ImportExportModelAdmin):
    resource_class = SKUResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)


        new_skus = resource.get_queryset()
        print("--------------", new_skus)


        for sku in new_skus:
            print("--------------", sku)
            sku.save()

        return result

    list_display = ('name', 'description','category')  # Add moxre fields if needed


class ManufacturerResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Manufacturer')  # Add the id field
    # category = fields.Field(
    #     column_name='Category',
    #     attribute='category',
    #     widget=ForeignKeyWidget(Category, 'name'))

    class Meta:
        model = Manufacturer  # Make sure to set the correct model here
        skip_unchanged = True
        report_skipped = False
        fields = ("name",)
        import_id_fields = ['name']

@admin.register(Manufacturer)
class ManufacturerAdmin(ImportExportModelAdmin):
    resource_class = ManufacturerResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)

        # Get the objects from the result of the import
        new_manufacturers = resource.get_queryset()
        print ("--------------",new_manufacturers)

        # Save each imported object to the database
        for manufacturer in new_manufacturers:
            print ("--------------",manufacturer)
            manufacturer.save()

        return result

    list_display = ('name',)  # Customize the list_display as needed
# tomize the displayed fields





class CountryResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Country')  # Add other fields if needed
    # category = fields.Field(
    #     column_name='Category',
    #     attribute='category',
    #     widget=ForeignKeyWidget(Category, 'name'))

    class Meta:
        model = Country
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'description',)  # Add more fields if needed
        import_id_fields = ['name']

@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)

        # Get the objects from the result of the import
        new_countries = resource.get_queryset()
        print("--------------", new_countries)

        # Save each imported object to the database
        for country in new_countries:
            print("--------------", country)
            country.save()

        return result

    list_display = ('name', 'description')  # A

class SeriesResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Series')  # Add other fields if needed
    # category = fields.Field(
    #     column_name='Category',
    #     attribute='category',
    #     widget=ForeignKeyWidget(Category, 'name'))
    class Meta:
        model = Series
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'description',)  # Add more fields if needed
        import_id_fields = ['name']

@admin.register(Series)
class SeriesAdmin(ImportExportModelAdmin):
    resource_class = SeriesResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)

        # Get the objects from the result of the import
        new_series = resource.get_queryset()
        print("--------------", new_series)

        # Save each imported object to the database
        for series in new_series:
            print("--------------", series)
            series.save()

        return result

    list_display = ('name', 'description')  # Add more fields if needed

class ModelNameResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Model name')  # Add other fields if needed
    category = fields.Field(
        column_name='Category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'name'))
    class Meta:
        model = ModelName
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'description', 'category')  # Add more fields if needed
        import_id_fields = ['name']

@admin.register(ModelName)
class ModelNameAdmin(ImportExportModelAdmin):
    resource_class = ModelNameResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)

        # Get the objects from the result of the import
        new_model_names = resource.get_queryset()
        print("--------------", new_model_names)

        # Save each imported object to the database
        for model_name in new_model_names:
            print("--------------", model_name)
            model_name.save()

        return result

    list_display = ('name','category')  # Add more fields if needed

# Register other models and their respective resources here if needed.

class ColorResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Color')  # Add other fields if needed
    category = fields.Field(
        column_name='Category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'name'))
    class Meta:
        model = Color
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'description','category')  # Add more fields if needed
        import_id_fields = []

@admin.register(Color)
class ColorAdmin(ImportExportModelAdmin):
    resource_class = ColorResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)

        # Get the objects from the result of the import
        new_colors = resource.get_queryset()
        print("--------------", new_colors)

        # Save each imported object to the database
        for color in new_colors:
            print("--------------", color)
            color.save()

        return result

    list_display = ('name', 'description','category')  # Add more fields if needed

class EUTypeApprovalResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Eu type')  # Add other fields if needed
    category = fields.Field(
        column_name='Category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'name'))
    class Meta:
        model = EUTypeApproval
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'description','category')  # Add more fields if needed
        import_id_fields = []  # Use 'name' as the identifier for deduplication

@admin.register(EUTypeApproval)
class EUTypeApprovalAdmin(ImportExportModelAdmin):
    resource_class = EUTypeApprovalResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)

        # Get the objects from the result of the import
        new_eu_type_approvals = resource.get_queryset()
        print("--------------", new_eu_type_approvals)

        # Save each imported object to the database
        for eu_type_approval in new_eu_type_approvals:
            print("--------------", eu_type_approval)
            eu_type_approval.save()

        return result

    list_display = ('name', 'description','category')
# @admin.register(BodyType)
# class BodyTypeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')

class SteeringPowerResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Steering power')  # Add other fields if needed
    category = fields.Field(
        column_name='Category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'name'))
    class Meta:
        model = SteeringPower
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'description','category')  # Add more fields if needed
        import_id_fields = []  # Use 'name' as the identifier for deduplication

@admin.register(SteeringPower)
class SteeringPowerAdmin(ImportExportModelAdmin):
    resource_class = SteeringPowerResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)

        # Get the objects from the result of the import
        new_steering_powers = resource.get_queryset()
        print("--------------", new_steering_powers)

        # Save each imported object to the database
        for steering_power in new_steering_powers:
            print("--------------", steering_power)
            steering_power.save()

        return result

    list_display = ('name', 'description')  # Add more fields if needed

class WheelsResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Wheels')  # Add other fields if needed
    category = fields.Field(
        column_name='Category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'name'))
    class Meta:
        model = Wheels
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'description', 'category')  # Add more fields if needed
        import_id_fields = []  # Use 'name' as the identifier for deduplication

@admin.register(Wheels)
class WheelsAdmin(ImportExportModelAdmin):
    resource_class = WheelsResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)

        # Get the objects from the result of the import
        new_wheels = resource.get_queryset()
        print("--------------", new_wheels)

        # Save each imported object to the database
        for wheels in new_wheels:
            print("--------------", wheels)
            wheels.save()

        return result

    list_display = ('name', 'description','category')

class CommunicationTerminalResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Communication terminal')  # Add other fields if needed
    category = fields.Field(
        column_name='Category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'name'))
    class Meta:
        model = CommunicationTerminal
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'description','category')  # Add more fields if needed
        import_id_fields = ['name']  # Use 'name' as the identifier for deduplication

@admin.register(CommunicationTerminal)
class CommunicationTerminalAdmin(ImportExportModelAdmin):
    resource_class = CommunicationTerminalResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)

        # Get the objects from the result of the import
        new_communication_terminals = resource.get_queryset()
        print("--------------", new_communication_terminals)

        # Save each imported object to the database
        for communication_terminal in new_communication_terminals:
            print("--------------", communication_terminal)
            communication_terminal.save()

        return result

    list_display = ('name', 'description','category')  # Add more fields if needed

class ScreenResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Screen')  # Add other fields if needed
    category = fields.Field(
        column_name='Category',
        attribute='category',
        widget=ForeignKeyWidget(Category, 'name'))
    class Meta:
        model = Screen
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'description', 'category')  # Add more fields if needed
        import_id_fields = []  # Use 'name' as the identifier for deduplication

@admin.register(Screen)
class ScreenAdmin(ImportExportModelAdmin):
    resource_class = ScreenResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)

        # Get the objects from the result of the import
        new_screens = resource.get_queryset()
        print("--------------", new_screens)

        # Save each imported object to the database
        for screen in new_screens:
            print("--------------", screen)
            screen.save()

        return result

    list_display = ('name', 'description','category')
class FactoryResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Factory name')  # Add other fields if needed
    category = fields.Field(
            column_name='Category',
            attribute='category',
            widget=ForeignKeyWidget(Category, 'name'))
    class Meta:
        model = Factory
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'description',)  # Add more fields if needed
        import_id_fields = ['name']  # Use 'name' as the identifier for deduplication

@admin.register(Factory)
class FactoryAdmin(ImportExportModelAdmin):
    resource_class = FactoryResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)

        # Get the objects from the result of the import
        new_factories = resource.get_queryset()
        print("--------------", new_factories)

        # Save each imported object to the database
        for factory in new_factories:
            print("--------------", factory)
            factory.save()

        return result

    list_display = ('name', 'description','category')  # Add more fields if needed

class LightsResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Lights')  # Add other fields if needed
    # category = fields.Field(
    #         column_name='Category',
    #         attribute='category',
    #         widget=ForeignKeyWidget(Category, 'name'))
    class Meta:
        model = Lights
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'description',)  # Add more fields if needed
        import_id_fields = ['name']  # Use 'name' as the identifier for deduplication

@admin.register(Lights)
class LightsAdmin(ImportExportModelAdmin):
    resource_class = LightsResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)

        # Get the objects from the result of the import
        new_lights = resource.get_queryset()
        print("--------------", new_lights)

        # Save each imported object to the database
        for lights in new_lights:
            print("--------------", lights)
            lights.save()

        return result

    list_display = ('name', 'description')  # Add more fields if needed

@admin.register(Vehicle)
class VehicleAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('get_sku_name', 'get_country', 'get_series', 'get_model_name', 'get_color', 'get_eu_type_approval',  'get_steering_power', 'get_wheels', 'get_screen', 'get_lights', 'get_factory_name', 'get_CommunicationTerminal', 'get_CargoCompartment',)

    def get_CommunicationTerminal(self, obj):
        return obj.communication_terminal.name if obj.communication_terminal else '-'
    get_CommunicationTerminal.short_description = 'CommunicationTerminal'

    def get_CargoCompartment(self, obj):
        return obj.cargo_compartment.name if obj.cargo_compartment else '-'
    get_CargoCompartment.short_description = 'CargoCompartment'

    def get_sku_name(self, obj):
        return obj.sku.name if obj.sku else '-'
    get_sku_name.short_description = 'Sku Name'

    def get_factory_name(self, obj):
        return obj.Factory_name.name if obj.Factory_name else '-'
    get_factory_name.short_description = 'Factory'

    def get_country(self, obj):
        return obj.country.name if obj.country else '-'
    get_country.short_description = 'Country'

    def get_series(self, obj):
        return obj.series.name if obj.series else '-'
    get_series.short_description = 'Series'

    def get_model_name(self, obj):
        return obj.model_name.name if obj.model_name else '-'
    get_model_name.short_description = 'Model Name'

    def get_color(self, obj):
        return obj.color.name if obj.color else '-'
    get_color.short_description = 'Color'

    def get_eu_type_approval(self, obj):
        return obj.eu_type.name if obj.eu_type else '-'
    get_eu_type_approval.short_description = 'EU Type Approval'

    # def get_body_type(self, obj):
    #     return obj.body_type.name if obj.body_type else '-'
    # get_body_type.short_description = 'Body Type'

    def get_steering_power(self, obj):
        return obj.steering_power.name if obj.steering_power else '-'
    get_steering_power.short_description = 'Steering Power'

    def get_wheels(self, obj):
        return obj.wheels.name if obj.wheels else '-'
    get_wheels.short_description = 'Wheels'

    def get_screen(self, obj):
        return obj.screen.name if obj.screen else '-'
    get_screen.short_description = 'Screen'

    def get_lights(self, obj):
        return obj.lights.name if obj.lights else '-'
    get_lights.short_description = 'Lights'

    class Media:
        js = ("js/data.js",)



    def vehicle_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;" />', obj.image.url)
        else:
            return '-'
    vehicle_image.short_description = 'Vehicle Image'
    def save_model(self, request, obj, form, change):
        if not change:  # Check if it's a new object being created
            # Save the current Vehicle instance
            super().save_model(request, obj, form, change)

            # Create a new order instance for the vehicle
            new_order = newOrder.objects.create(
                vehicle=obj,  # Link the newOrder instance to the saved Vehicle instance
                dealer=request.user,  # Link the dealer to the current user who is saving the vehicle
                # factory=obj.factory,  # Link the factory to the vehicle's factory
                status='W',  # Set the initial status to 'Waiting for Receive'
            )

            # Save the newOrder instance to add it to the database
            new_order.save()
            print("RETERRDFFGGFDG",obj.orderer_email)
            # Create and add a historical record
            history_instance = vehiclehystory.objects.create(
                timestamp=timezone.now(),
                description="The vehicle order has been forwarded to the factory.",
                historical_note="The vehicle order has been forwarded to the factory.",
                vehicle=obj,
                owner_email=obj.orderer_email,
                  # Link the historical record to the saved Vehicle instance
            )

            # Save the historical record instance to add it to the database
            history_instance.save()

            # Display a success message
            messages.success(request, 'New order has been added to the factory. The factory must update the status.')
        else:
            # For existing objects, save as usual without triggering additional actions
            super().save_model(request, obj, form, change)




class cargoResource(resources.ModelResource):
    name = fields.Field(attribute='name', column_name='Cargo compartment')  # Add other fields if needed
    category = fields.Field(
            column_name='Category',
            attribute='category',
            widget=ForeignKeyWidget(Category, 'name'))
    class Meta:
        model = CargoCompartment
        skip_unchanged = True
        report_skipped = False
        fields = ('name', 'description', 'category')  # Add more fields if needed
        import_id_fields = []  # Use 'name' as the identifier for deduplication

@admin.register(CargoCompartment)
class LightsAdmin(ImportExportModelAdmin):
    resource_class = cargoResource

    def import_resource(self, request, resource, *args, **kwargs):
        result = super().import_resource(request, resource, *args, **kwargs)

        # Get the objects from the result of the import
        new_lights = resource.get_queryset()
        print("--------------", new_lights)

        # Save each imported object to the database
        for lights in new_lights:
            print("--------------", lights)
            lights.save()

        return result

    list_display = ('name', 'description')  # Add more fields if needed
