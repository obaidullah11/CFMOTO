from rest_framework import generics
from .models import Category,Subcategory,Product,SparePart,Mileage,History,ServiceImage,ProductService,Repairing,Maintenance,CheckMaintenance,newSparePart,CheckWarranty
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CategorySerializer,SubcategorySerializer,MileageSerializer,WarrantySerializer,ProductSerializer,SparePartSerializer,RepairingSerializer,getProductSerializer,ProductServiceSerializer,MechanicalNoteSerializer,HistorySerializer,ServiceImageSerializer,MaintenanceSerializer,CheckMaintenanceSerializer,newSparePartSerializer
from simple_history.models import HistoricalRecords
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
@api_view(['POST'])
def create_repairing(request):
    serializer = RepairingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def create_warranty(request):
    serializer = WarrantySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print("Warranty created successfully!")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print("Error creating warranty:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_active_check_warranty(request, sku):
    try:
        check_warranty = CheckWarranty.objects.get(product_id__sku=sku, is_active=True)
        serializer = CheckWarrantySerializer(check_warranty)
        return Response(serializer.data)
    except CheckWarranty.DoesNotExist:
        return Response({"message": "No active warranty found."}, status=200)

# api to check maintainence availible or not



@api_view(['GET'])
def get_active_check_maintenance(request, sku):
    try:
        check_maintenance = CheckMaintenance.objects.get(product_id__sku=sku, is_active=True)
        serializer = CheckMaintenanceSerializer(check_maintenance)
        return Response(serializer.data)
    except :
        return Response({"message": "No active  maintenance found ."}, status=200)
# api to create maintainence


@api_view(['POST'])
def create_maintenance(request):
    data = request.data
    serializer = MaintenanceSerializer(data=data)
    if serializer.is_valid():
        check_maintenance = serializer.validated_data.get('maintanence_id')
        check_maintenance_id = check_maintenance.id if check_maintenance else None
        print(check_maintenance_id)  # Print the value for debugging
        if check_maintenance_id is not None:
            CheckMaintenance.objects.filter(id=check_maintenance_id).update(is_active=False)
        mentain = serializer.save()
        parts = data.get("replace_parts","").split(",")

        for i in parts:
            mentain.replace_parts.add(newSparePart.objects.get(id=int(i)))

        mentain.save()

        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)

@api_view(['GET'])
def newsparepart_detail(request, sku):
    newspareparts = newSparePart.objects.filter(product__sku=sku)

    if newspareparts.exists():
        serializer = newSparePartSerializer(newspareparts, many=True)
        return Response(serializer.data)
    else:
        message = f"No newSparePart instances found for sku: {sku}"
        return Response(status=404, data={"message": message})



# @api_view(['POST'])
# def create_warranty_claim(request):
#     serializer = warrantySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=201)
#     return Response(serializer.errors, status=400)
# @api_view(['GET'])
# def get_warranty_claims(request):
#     warranty_claims = WarrantyClaim.objects.all()
#     serializer = warrantySerializer(warranty_claims, many=True)
#     return Response(serializer.data)




# @api_view(['PUT'])
# def update_warranty_claim(request, claim_id):
#     try:
#         warranty_claim = WarrantyClaim.objects.get(id=claim_id)
#     except WarrantyClaim.DoesNotExist:
#         return Response({"message": "Warranty claim does not exist"}, status=404)

#     serializer = warrantySerializer(warranty_claim, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=400)
# class CategoryListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
# @api_view(['GET', 'POST'])
# def maintenance_list(request):
#     if request.method == 'GET':
#         maintenance = Maintenance.objects.all()
#         serializer = MaintenanceSerializer(maintenance, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = MaintenanceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def maintenance_detail(request, pk):
#     try:
#         maintenance = Maintenance.objects.get(pk=pk)
#     except Maintenance.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         serializer = MaintenanceSerializer(maintenance)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = MaintenanceSerializer(maintenance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         maintenance.delete()
#         return Response(status=204)
# @csrf_exempt


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryList(generics.ListAPIView):
    serializer_class = SubcategorySerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Subcategory.objects.filter(parent_id=category_id)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['category_id'] = self.kwargs['category_id']
        return context




# @csrf_exempt
# def create_product(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         serializer = ProductSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class SubcategoryCreateView(generics.CreateAPIView):
    serializer_class = SubcategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubcategoryDetailView(generics.RetrieveAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
class SubcategoryListView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
class SubcategoryByParentView(generics.ListAPIView):
    serializer_class = SubcategorySerializer

    def get_queryset(self):
        parent_id = self.kwargs['parent_id']
        return Subcategory.objects.filter(parent__id=parent_id)

# class SparePartSearchView(generics.ListAPIView):
#     serializer_class = SparePartSerializer

#     def get_queryset(self):
#         model_id = self.request.query_params.get('model_id', None)
#         if model_id is not None:
#             queryset = SparePart.objects.filter(model_id=model_id)
#             return queryset
class SparePartList(generics.ListCreateAPIView):
    queryset = SparePart.objects.all()
    serializer_class = SparePartSerializer

class SparePartDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SparePart.objects.all()
    serializer_class = SparePartSerializer

@api_view(['GET'])
def get_product_by_vin(request, vin_code):
    try:
        product = Product.objects.get(vin_code=vin_code)
        serializer = getProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({'message': 'Product not found'}, status=404)

@api_view(['POST'])
def add_service(request):
    serializer = addServiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_services(request):
    services = Maintainence_panel.objects.all()
    serializer = addServiceSerializer(Maintainence_panel, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def product_service_create(request):
#     data = request.data if isinstance(request.data, list) else [request.data]
#     serializer = ProductServiceSerializer(data=data, many=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def mechanical_note_create(request):
    serializer = MechanicalNoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {'success': 'MechanicalNote created successfully'}
        return Response(data=message, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def create_history(request):
    serializer = HistorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message = {'message': 'History instance created successfully.'}
        response_data = {**serializer.data, **message}
        return Response(response_data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_history_by_product(request, product_id):
    try:
        history = History.objects.filter(product_id=product_id).order_by('timestamp')
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data, status=200)
    except History.DoesNotExist:
        message = {'error': f'No history available for product with id {product_id}.'}
        return Response(message, status=404)
# views.py
# @api_view(['GET'])
# def (request, product_id):
#     try:
#         product = Product.objects.get(product=product_id)
#         print("=====>",product)
#         history = product.services.all()
#         print("=====>",history)
#         serializer = HistorySerializer(history, many=True)
#         print("=====>",serializer.data)
#         return Response(serializer.data, status=200)
#     except Product.DoesNotExist:
#         message = {'error': f'Product with id {product_id} does not exist.'}
#         return Response(message, status=404)




@api_view(['POST'])
def create_service_image(request):
    product_id = request.data.get('product')
    try:
        service_image, created = ServiceImage.objects.get_or_create(product_id=product_id)
        serializer = ServiceImageSerializer(service_image, data=request.data)
        if serializer.is_valid():
            serializer.save()
            if created:
                return Response({"message": "ServiceImage created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": "ServiceImage updated successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return Response({"message": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)


# @api_view(['POST'])
# def service_create(request):
#     if request.method == 'POST':
#         serializer = addServiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
# def service_list(request):
#     if request.method == 'GET':
#         services = Service.objects.all()
#         serializer = addServiceSerializer(services, many=True , context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_product_service(request):
    serializer = ProductServiceSerializer(data=request.data, many=True)
    if serializer.is_valid():
        instances = serializer.save()
        return Response({'message': f'{len(instances)} product services created successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_service_images(request, product_id):
    try:
        service_images = ServiceImage.objects.filter(product_id=product_id)
        if service_images.exists():
            serializer = ServiceImageSerializer(service_images, many=True)
            return Response(serializer.data)
        else:
            return Response(status=404)
    except ServiceImage.DoesNotExist:
        return Response(status=404)

# @api_view(['POST'])
# def create_product_service(request):
#     if request.method == 'POST':
#         serializer = ProductServiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)@api_view(['POST'])
# def create_product_total_time(request):
#     serializer = ProductTotalTimeSerializer(data=request.data, many=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'message': 'Product total time created successfully'}, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# new maintainence part








# from .serializers import ServiceSerializer

# views.py


class MileageList(generics.ListAPIView):
    queryset = Mileage.objects.all()
    serializer_class = MileageSerializer


# class ServiceList(generics.ListAPIView):
#     serializer_class = ServiceListSerializer

#     def get_queryset(self):
#         sku_name = self.kwargs['sku_name']  # Retrieve SKU name from URL parameter
#         target_mileage_str = self.kwargs.get('target_mileage')  # Retrieve target mileage as a string from URL parameter

#         # Try to convert target_mileage_str to an integer
#         try:
#             target_mileage = int(target_mileage_str)
#         except ValueError:
#             # Handle the case where target_mileage_str is not a valid integer
#             return Service.objects.none()

#         # Retrieve the Service records filtered by SKU name and target_mileage
#         queryset = Service.objects.filter(SKU__name=sku_name, mileage__Mileage=target_mileage)

#         # Find the record with mileage closest to the specified value
#         nearest_record = None
#         min_distance = float('inf')

#         for service in queryset:
#             mileage_difference = abs(int(service.mileage.Mileage) - target_mileage)
#             if mileage_difference < min_distance:
#                 min_distance = mileage_difference
#                 nearest_record = service

#         # Return the nearest record or None if no records were found
#         return [nearest_record] if nearest_record else []

#     # Rest of your view code...



# class ServiceList(generics.ListAPIView):
#     serializer_class = ServiceListSerializer

#     def get_queryset(self):
#         sku_name = self.kwargs['sku_name']  # Retrieve SKU name from URL parameter
#         mileage_value = self.kwargs['mileage_value']  # Retrieve Mileage value from URL parameter

#         # Retrieve the Service records filtered by SKU name and Mileage value
#         queryset = Service.objects.filter(SKU__name=sku_name, mileage__Mileage=mileage_value)

#         # Find the record with mileage closest to the specified value
#         nearest_record = None
#         min_distance = float('inf')

#         for service in queryset:
#             mileage_difference = abs(service.mileage.Mileage - mileage_value)
#             if mileage_difference < min_distance:
#                 min_distance = mileage_difference
#                 nearest_record = service

#         # Return the nearest record or None if no records were found
#         return [nearest_record] if nearest_record else []
