from rest_framework import serializers
from .models import Category,Product,Subcategory,Maintenance_List,Mileage,ProductService,Warranty,MechanicalNote,Repairing,ServiceImage,newSparePart,CheckWarranty
# from simple_history.models import HistoricalRecords
from users.models import User

# class warrantySerializer(serializers.ModelSerializer):
#     product_sku = serializers.CharField(source='product_id.sku', read_only=True)

#     class Meta:
#         model = WarrantyClaim
#         fields = ['product_sku', 'mileage', 'failure_description', 'repair_parts', 'cause', 'repair_remarks', 'review', 'remark', 'created_at', 'image', 'video']

# serializers.py
class ProductServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductService
        fields = '__all__'

class ProductServiceListSerializer(serializers.ListSerializer):
    child = ProductServiceSerializer()

class MaintenanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance_List
        fields = '__all__'
        depth = 1  

# class MaintenanceSerializer(serializers.ModelSerializer):
#     product_sku = serializers.ReadOnlyField(source='product_id.sku')

#     class Meta:
#         model = Maintenance
#         fields = ('id', 'maintanence_id', 'product_id', 'product_sku', 'mileage', 'customer_description', 'receiver_description', 'feedback','video','picture','time')
class RepairingSerializer(serializers.ModelSerializer):
    product_sku = serializers.ReadOnlyField(source='product_id.sku')

    class Meta:
        model = Repairing
        fields = ('product_id', 'product_sku', 'mileage', 'customer_description', 'receiver_description', 'feedback','video','picture','time')
class WarrantySerializer(serializers.ModelSerializer):
    product_sku = serializers.ReadOnlyField(source='product_id.sku')

    class Meta:
        model = Warranty
        fields = ('product_id', 'product_sku', 'mileage', 'cause', 'review', 'remarks','failure_description','video','picture','time')
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'parent')
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'sku', 'vin_code', 'manufacture', 'country', 'series', 'model_name', 'factory_name', 'color', 'eu_type_approval', 'body_type', 'steering_power', 'wheels', 'screen', 'lights', 'cargo_compartments', 'communication_terminal', 'date_of_manufacture', 'orderer', 'orderer_phone', 'orderer_email', 'importer', 'dealer', 'category', 'sub_category', 'image']
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
# class SparePartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SparePart
#         fields = ('model_id', 'id_code', 'part_name', 'description')


# class HistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = History
#         fields = ['id', 'product', 'timestamp', 'description']
class getProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(read_only=True)
    sub_category = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'public_id', 'sku', 'vin_code', 'manufacture', 'country', 'series', 'model_name', 'factory_name', 'color', 'eu_type_approval', 'body_type', 'steering_power', 'wheels', 'screen', 'lights', 'cargo_compartments', 'communication_terminal', 'date_of_manufacture', 'orderer', 'orderer_phone', 'orderer_email', 'importer', 'dealer', 'category', 'sub_category', 'image']

####done###
class ProductServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductService
        fields = ['is_active', 'comment', 'executed', 'fill', 'value', 'product', 'name', 'time_spent', 'user']
##########
class MechanicalNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MechanicalNote
        fields = ('id', 'product', 'note', 'date_created','user')


# class HistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = History
#         fields = ('id', 'timestamp', 'description', 'product','user')



class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ('product', 'image1', 'image2', 'image3', 'image4')




class ProductServiceSerializer(serializers.ModelSerializer):
    total_time_required = serializers.DurationField(read_only=True)

    class Meta:
        model = ProductService
        fields = '__all__'
class CheckWarrantySerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckWarranty
        fields = ('id', 'product_id', 'warranty_name', 'is_active')

    def validate(self, attrs):
        is_active = attrs.get('is_active')
        product_id = attrs.get('product_id')

        if is_active:
            # Check if there is already an active record for the same product
            if CheckWarranty.objects.filter(product_id=product_id, is_active=True).exists():
                raise serializers.ValidationError("There is already an active record for this product.")

        return attrs


# class CheckMaintenanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CheckMaintenance
#         fields = ('id', 'product_id', 'maintenance_name', 'is_active')

    # def validate(self, attrs):
    #     is_active = attrs.get('is_active')
    #     product_id = attrs.get('product_id')

    #     if is_active:
    #         # Check if there is already an active record for the same product
    #         if CheckMaintenance.objects.filter(product_id=product_id, is_active=True).exists():
    #             raise serializers.ValidationError("There is already an active record for this product.")

    #     return attrs

class addServiceSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    def get_images(self, service):
        # Combine all image fields into a list
        images = [service.image_1, service.image_2, service.image_3, service.image_4]
        # Filter out any empty images
        images = [image for image in images if image]
        # Get the URLs for each image
        urls = [self.context['request'].build_absolute_uri(image.url) for image in images]
        return urls

    class Meta:
        model = Maintenance_List
        fields = ['id', 'name', 'instructions', 'instruction_active','fill_active','value_active', 'images', 'video']

class newSparePartSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = newSparePart
        fields = ['id','product', 'model_id', 'id_code', 'part_name', 'description']

    def get_product(self, obj):
        return obj.product.sku



# class ServiceDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Maintenance_List
#         fields = '__all__'

# class ServiceListSerializer(serializers.ModelSerializer):
#     # Define the serializer fields that you want to include in the response
#     mileage = serializers.IntegerField(source='mileage.Mileage')
#     sku = serializers.CharField(source='SKU.name')

#     class Meta:
#         model = Maintenance_List
#         fields = (
#             'Maintenance_list_name',
#             'instructions',
#             'Maintainencepoint',
#             'mileage',
#             'Year',
#             'Factory_name',
#             'sku',
#             'instruction_active',
#             'fill_active',
#             'value_active',
#             'image_1',
#             'image_2',
#             'image_3',
#             'image_4',
#             'video',
#         )




class MileageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mileage
        fields = ['id','Mileage']
# class MaintenanceListPointSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MaintenanceListPoint
#         fields = ['id', 'Maintenance_List_Point_name', 'maintenance_points', 'my_order']