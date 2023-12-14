from django.contrib import admin
from django.utils.html import format_html
from .models import TemporaryMechanicalNote,Category,Subcategory,bulletins_completed,temporarymaintenance,temporaryWarranty,temporaryRepairing,Product,ProductService,Vincode, Bulletins ,Maintenance_List,Maintainencepoint,Warranty,Mileage,Year,ServiceImage,Repairing,Vehicle,newSparePart,CheckWarranty
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from adminsortable2.admin import SortableTabularInline
from adminsortable2.admin import SortableStackedInline
from django.contrib import admin
from django.urls import reverse
from django.db.models import Count
from import_export.widgets import DecimalWidget
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
# from .serializers import ProductSerializer
from adminsortable2.admin import SortableAdminMixin
from django import forms
from import_export import resources


@admin.register(temporarymaintenance)
class temporarymaintenanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_name','executed', 'user_name','time_spent_s','fill','value','comment')
    list_filter = ('user', 'product')
    search_fields = ('name', 'comment', 'product__name', 'product__sku', 'user__username')
    ordering = ('-id',)

    def time_spent_s(self, obj):
        return f"{obj.time_spent}s" if obj.time_spent else "0s"
    def user_name(self, obj):
        return obj.user.name

    def product_name(self, obj):
        return obj.product.model_name

    user_name.short_description = 'User'
    product_name.short_description = 'Product'


@admin.register(temporaryRepairing)

class tempRepairingAdmin(admin.ModelAdmin):
    list_display = [ 'product_id', 'mileage', 'customer_description', 'receiver_description', 'feedback']
    list_filter = ['product_id__sku']
    exclude=['picture','video']
    # search_fields = ['repairing_id', 'product_id__sku', 'customer_description']
    ordering = ['-id']
    def product_id(self, obj):
        return obj.product.sku
    def get_replace_parts_names(self, obj):
        return ", ".join([part.part_name for part in obj.replace_parts.all()])
    def time_spent_s(self, obj):
        return f"{obj.time}s"

    get_replace_parts_names.short_description = 'Replace Parts'

    # Optionally, override the save_model method to perform custom logic
    def save_model(self, request, obj, form, change):
        # Custom logic to be executed when saving the model instance
        super().save_model(request, obj, form, change)
@admin.register(temporaryWarranty)        
class tempWarrantyAdmin(admin.ModelAdmin):
    list_display = [ 'mileage','product_id', 'cause', 'review', 'remarks','failure_description']
    list_filter = ['product_id__sku']
    search_fields = ['product_id__sku','failure_description']
    ordering = ['-id']

    def get_replace_parts_names(self, obj):
        return ", ".join([part.part_name for part in obj.replace_parts.all()])

    get_replace_parts_names.short_description = 'Replace Parts'
    # def time_spent_s(self, obj):
    #     return f"{obj.time}s"

    # Optionally, override the save_model method to perform custom logic
    def save_model(self, request, obj, form, change):
        # Custom logic to be executed when saving the model instance
        super().save_model(request, obj, form, change)
class VincodeAdmin(ImportExportModelAdmin):
    list_display = ('vincode', )
class BulletinsCompletedAdmin(admin.ModelAdmin):
    list_display = ('id', 'bulletins_id', 'bulletins_mechanical_note')  # Customize as needed
    search_fields = ['bulletins_id']
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    
    # Add search fields if you have related fields

# Register your models here
admin.site.register(bulletins_completed, BulletinsCompletedAdmin)

class BulletinsAdmin(admin.ModelAdmin):
    list_display = ('id','bulletins_name', 'Date')
    # id.short_description = 'bulletins_id'


class MaintainencepointResource(resources.ModelResource):
    class Meta:
        model = Maintainencepoint
        import_id_fields = ['Maintainencepoint_name']
@admin.register(Maintainencepoint)
class MaintainencepointAdmin(ImportExportModelAdmin):
    resource_class = MaintainencepointResource
    list_display = ('Point_id', 'Maintainencepoint_name', 'instructions', 'instruction_active',)
    list_filter = ( 'instruction_active', )
    search_fields = ('Maintainencepoint_name',)
    exclude=('my_order',)
    class Media:
        js = ('js/file_privew.js',) 



@admin.register(Maintenance_List)
class MaintenanceListAdmin(admin.ModelAdmin):

    list_display = ('Maintenance_list_id', 'Maintenance_list_name', 'Maintainence_description')
    # search_fields = ('Maintenance_list_name', 'Maintainence_description')
    # filter_vertical  = ('Maintenance_List_Point_name',)
    # ordering = ('my_order',)
    # raw_id_fields = ('Maintenance_List_Point_name',)
    def __str__(self):
        return self.Maintenance_list_name
    def display_maintenance_points(self, obj):
        return ", ".join([point.Maintainencepoint_name for point in obj.Maintenance_List_Point_name.all()])
    display_maintenance_points.short_description = ''

    # def save(self, *args, **kwargs):
    #     # Call the parent class's save method
    #     super(Maintenance_List, self).save(*args, **kwargs)

    #     # Create a corresponding MaintenancePointOrder record
    #     MaintenancePointOrder.objects.create(
    #         maintenance_list_name=self.Maintenance_list_name,
    #         maintenance_point_name="Point Name",  # Replace with the actual point name
    #         order=1  # Replace with the appropriate order value
    #     )


@admin.register(Repairing)

class RepairingAdmin(admin.ModelAdmin):
    list_display = ['repairing_id', 'product_id', 'mileage', 'customer_description', 'receiver_description', 'feedback']
    list_filter = ['product_id__sku','repairing_id']
    # search_fields = ['repairing_id', 'product_id__sku', 'customer_description']
    ordering = ['-id']
    def product_id(self, obj):
        return obj.product.sku
    def get_replace_parts_names(self, obj):
        return ", ".join([part.part_name for part in obj.replace_parts.all()])
    def time_spent_s(self, obj):
        return f"{obj.time}s"

    get_replace_parts_names.short_description = 'Replace Parts'

    # Optionally, override the save_model method to perform custom logic
    def save_model(self, request, obj, form, change):
        # Custom logic to be executed when saving the model instance
        super().save_model(request, obj, form, change)
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ['Warranty_id', 'mileage','product_id', 'cause', 'review', 'remarks','failure_description']
    list_filter = ['product_id__sku']
    search_fields = ['Warranty_id','product_id__sku','failure_description']
    ordering = ['-id']

    def get_replace_parts_names(self, obj):
        return ", ".join([part.part_name for part in obj.replace_parts.all()])

    get_replace_parts_names.short_description = 'Replace Parts'
    # def time_spent_s(self, obj):
    #     return f"{obj.time}s"

    # Optionally, override the save_model method to perform custom logic
    def save_model(self, request, obj, form, change):
        # Custom logic to be executed when saving the model instance
        super().save_model(request, obj, form, change)
@admin.register(newSparePart)
class SparePartAdmin(ImportExportModelAdmin):
    list_display = ['id', 'product_sku', 'model_id', 'id_code', 'part_name']
    list_filter = ['product__sku']  # Use product__sku for filtering
    search_fields = ['model_id', 'id_code', 'part_name']

    def product_sku(self, obj):
        return obj.product.sku

    product_sku.short_description = 'Product SKU'

class ServiceImageAdmin(admin.ModelAdmin):
    def image1_tag(self, obj):
        if obj.image1:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image1.url))
        else:
            return '-'
    image1_tag.short_description = 'Image 1'

    def image2_tag(self, obj):
        if obj.image2:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image2.url))
        else:
            return '-'
    image2_tag.short_description = 'Image 2'

    def image3_tag(self, obj):
        if obj.image3:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image3.url))
        else:
            return '-'
    image3_tag.short_description = 'Image 3'

    def image4_tag(self, obj):
        if obj.image4:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image4.url))
        else:
            return '-'
    image4_tag.short_description = 'Image 4'

    def product_vin_code(self, obj):
        return obj.product.vin_code


    list_display = ('id', 'product_vin_code', 'image1_tag', 'image2_tag', 'image3_tag', 'image4_tag')
    list_filter = ('product__vin_code',)
    search_fields = ('product__vin_code', 'product__name',)
    # date_hierarchy = 'product__created_at'
@admin.register(ProductService)
class ProductServiceAdmin(admin.ModelAdmin):
     list_display = ('id', 'name', 'product_name', 'is_active', 'executed', 'user_name','time_spent_s','fill','value','comment')
     list_filter = ('user', 'product')
     search_fields = ('name', 'comment', 'product__name', 'product__sku', 'user__username')
     ordering = ('-id',)

     def time_spent_s(self, obj):
         return f"{obj.time_spent}s" if obj.time_spent else "0s"
     def user_name(self, obj):
         return obj.user.name

     def product_name(self, obj):
         return obj.product.model_name

     user_name.short_description = 'User'
     product_name.short_description = 'Product'
class MaintainencepointAdmin(admin.ModelAdmin):
    list_display = ('Point_id','Maintainencepoint_name', 'instruction_active', 'fill_active', 'value_active', 'display_image_1', 'display_image_2', 'display_image_3', 'display_image_4', 'display_video_thumbnail')
    list_filter = ('instruction_active', 'fill_active', 'value_active')
    search_fields = ('point_name',)



    def display_image_1(self, obj):
        if obj.image_1:
            return format_html('<img src="{}" height="50"/>'.format(obj.image_1.url))
        else:
            return ''
    display_image_1.short_description = 'Image 1'

    def display_image_2(self, obj):
        if obj.image_2:
            return format_html('<img src="{}" height="50"/>'.format(obj.image_2.url))
        else:
            return ''
    display_image_2.short_description = 'Image 2'

    def display_image_3(self, obj):
        if obj.image_3:
            return format_html('<img src="{}" height="50"/>'.format(obj.image_3.url))
        else:
            return ''
    display_image_3.short_description = 'Image 3'

    def display_image_4(self, obj):
        if obj.image_4:
            return format_html('<img src="{}" height="50"/>'.format(obj.image_4.url))
        else:
            return ''
    display_image_4.short_description = 'Image 4'
    def display_image_5(self, obj):
        if obj.image_5:
            return format_html('<img src="{}" height="50"/>'.format(obj.image_5.url))
        else:
            return ''
    display_image_5.short_description = 'Image 5'
    def display_video1_thumbnail(self, obj):
        return self._display_video_thumbnail(obj, 'video1')

    def display_video2_thumbnail(self, obj):
        return self._display_video_thumbnail(obj, 'video2')

    def display_video3_thumbnail(self, obj):
        return self._display_video_thumbnail(obj, 'video3')

    def _display_video_thumbnail(self, obj, field_name):
        video_url = getattr(obj, field_name)
        if video_url:
            # Extract the video ID from the URL
            video_id = video_url.split('/')[-1]
            thumbnail_url = f'https://img.youtube.com/vi/{video_id}/0.jpg'  # Assuming YouTube video
            return format_html('<a href="{}" target="_blank"><img src="{}" height="100"/></a>', video_url, thumbnail_url)
        return ''

    display_video1_thumbnail.short_description = 'Video 1 Thumbnail'
    display_video2_thumbnail.short_description = 'Video 2 Thumbnail'
    display_video3_thumbnail.short_description = 'Video 3 Thumbnail'

    # def display_video_thumbnail(self, obj):
    #     if obj.video:
    #         # Extract the video ID from the URL
    #         video_id = obj.video.split('/')[-1]
    #         thumbnail_url = f'https://img.youtube.com/vi/{video_id}/0.jpg'  # Assuming YouTube video
    #         video_url = obj.video
    #         return format_html('<a href="{}" target="_blank"><img src="{}" height="100"/></a>', video_url, thumbnail_url)
    #     return ''
    # display_video_thumbnail.short_description = 'Video Thumbnail'

class MileageAdmin(ImportExportModelAdmin):
    list_display = ('Mileage',)
    search_fields = ['Mileage']

admin.site.register(Mileage, MileageAdmin)
class YearAdmin(ImportExportModelAdmin):
    list_display = ('Year',)
    search_fields = ['Year']

admin.site.register(Year, YearAdmin)
admin.site.register(ServiceImage, ServiceImageAdmin)

admin.site.register(Warranty,WarrantyAdmin)
admin.site.site_header = 'CFMOTO'
# admin.site.register(Mileage)
admin.site.register(Vincode)
admin.site.register(Bulletins, BulletinsAdmin)
# admin.site.register(Vincode, VincodeAdmin)

admin.site.register(TemporaryMechanicalNote)
