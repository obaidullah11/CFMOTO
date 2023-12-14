from rest_framework import generics
from .models import TemporaryMechanicalNote,temporarymaintenance,Category,temporaryWarranty,temporaryRepairing,Subcategory,Product,bulletins_completed,Maintenance_List,Bulletins,Mileage,ServiceImage,ProductService,Repairing,newSparePart,CheckWarranty
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import  TemporaryMaintenanceSerializer,BulletinsCompletedSerializer,TemporaryMechanicalNoteSerializer,tempWarrantySerializer,tempRepairingSerializer,MaintenanceListSerializer,BulletinsSerializer,ProductServiceListSerializer,addServiceSerializer,CategorySerializer,SubcategorySerializer,MileageSerializer,WarrantySerializer,ProductSerializer,RepairingSerializer,getProductSerializer,ProductServiceSerializer,MechanicalNoteSerializer,ServiceImageSerializer,newSparePartSerializer
from simple_history.models import HistoricalRecords
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from django.http import JsonResponse

@api_view(['POST'])  # Changed from 'DELETE' to 'POST'
def delete_temporary_maintenance_by_product(request, product_id):
    try:
        # Get all maintenance records for the given product_id
        maintenance_records = temporarymaintenance.objects.filter(product_id=product_id)
        if not maintenance_records:
            return Response({'message': 'No records found'}, status=status.HTTP_404_NOT_FOUND)

        # Delete the records
        maintenance_records.delete()
        return Response({'message': 'Records deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_temporary_maintenance(request):
    if request.method == 'POST':
        data = request.data  # Get the list of dictionaries from the request

        # Ensure that the data is a list
        if not isinstance(data, list):
            return Response({'error': 'Data must be a list of dictionaries'}, status=status.HTTP_400_BAD_REQUEST)

        # Serialize each dictionary in the list and save
        serialized_data = []
        for item_data in data:
            serializer = TemporaryMaintenanceSerializer(data=item_data)
            if serializer.is_valid():
                serializer.save()
                serialized_data.append(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serialized_data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_temporary_maintenance_by_product(request, product_id):
    try:
        maintenance_records = temporarymaintenance.objects.filter(product_id=product_id)
        serializer = TemporaryMaintenanceSerializer(maintenance_records, many=True)

        if not maintenance_records:
            # Return a response with status 200 and an empty data list
            return Response([], status=status.HTTP_200_OK)

        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def create_temporary_mechanical_note(request):
    if request.method == 'POST':
        serializer = TemporaryMechanicalNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])  # Change to POST
def delete_temporary_mechanical_note_by_product(request, product_id):
    try:
        # Find the note by product_id
        note = TemporaryMechanicalNote.objects.get(product_id=product_id)
    except TemporaryMechanicalNote.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # No need to check request.method == 'DELETE' as it's now a POST request
    note.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET'])
def get_temporary_mechanical_note_by_product(request, product_id):
    try:
        # Find the note by product_id
        note = TemporaryMechanicalNote.objects.get(product_id=product_id)

        # Serialize the note object
        serializer = TemporaryMechanicalNoteSerializer(note)
        return Response(serializer.data)
    except TemporaryMechanicalNote.DoesNotExist:
        # Return a response with status 200 and an empty data object
        return Response({}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def delete_temporary_repairing(request, pk):
    if request.method == 'POST':
        try:
            temporary_repairing = temporaryRepairing.objects.get(pk=pk)
            temporary_repairing.delete()
            return Response({'message': 'Record deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except temporaryrepairing.DoesNotExist:
            return Response({'error': 'Record does not exist'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def delete_temporary_warranty(request, pk):
    try:
        warranty = temporaryWarranty.objects.get(pk=pk)
        warranty.delete()
        return Response({'message': 'Temporary warranty record deleted successfully'})
    except temporaryWarranty.DoesNotExist:
        return Response({'error': 'Temporary warranty data not found for the given Warranty ID'}, status=404)
@api_view(['GET'])
def get_temporary_repairing_by_product_id(request, product_id):
    try:
        repairing = temporaryRepairing.objects.get(product_id=product_id)
        serializer = tempRepairingSerializer(repairing)
        return Response(serializer.data)
    except temporaryRepairing.DoesNotExist:
        return Response({'error': 'Temporary repairing data not found for the given product ID'}, status=404)


@api_view(['GET'])
def get_temporary_warranty_by_product_id(request, product_id):
    try:
        warranty = temporaryWarranty.objects.get(product_id=product_id)
        serializer = tempWarrantySerializer(warranty)
        return Response(serializer.data)
    except temporaryWarranty.DoesNotExist:
        return Response({'error': 'Temporary warranty not found for the given product ID'}, status=404)


@api_view(['POST'])
def temp_create_repairing(request):
    product_id = request.data.get('product_id')  # Assuming 'product_id' is the field name
    existing_record = temporaryRepairing.objects.filter(product_id=product_id).first()

    if existing_record:
        # If record exists, update it
        serializer = tempRepairingSerializer(existing_record, data=request.data)
    else:
        # If record does not exist, create a new one
        serializer = tempRepairingSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def temp_create_warranty(request):
    product_id = request.data.get('product_id')  # Assuming 'product_id' is the field name
    existing_record = temporaryWarranty.objects.filter(product_id=product_id).first()

    if existing_record:
        # If record exists, update it
        serializer = tempWarrantySerializer(existing_record, data=request.data)
    else:
        # If record does not exist, create a new one
        serializer = tempWarrantySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        print("Warranty created/updated successfully!")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print("Error creating/updating warranty:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_bulletins_completed(request):
    if request.method == 'POST':
        serializer = BulletinsCompletedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_bulletins_by_vin(request, vin_code):
    bulletins = Bulletins.objects.filter(vincode__vincode=vin_code)
    serializer = BulletinsSerializer(bulletins, many=True)
    return Response(serializer.data)




class MaintenanceListPointByFactoryView(APIView):
    def get(self, request, factory_name, format=None):
        # Retrieve all Maintenance_List objects with the specified Factory_name
        maintenance_lists = Maintenance_List.objects.filter(Factory_name__name=factory_name)

        # Initialize a list to store Maintenance_List_Point_name values
        maintenance_list_points = []

        # Iterate through the Maintenance_List objects and collect all fields of Maintenance_List_Point_name
        for maintenance_list in maintenance_lists:
            maintenance_list_points.extend(maintenance_list.Maintenance_List_Point_name.values())

        return Response(maintenance_list_points)
class MaintenanceListByFactoryView(generics.ListAPIView):
    serializer_class = MaintenanceListSerializer

    def get_queryset(self):
        factory_name = self.kwargs.get('factory_name')
        queryset = Maintenance_List.objects.filter(Factory_name__name=factory_name)
        if not queryset:
            raise NotFound(detail="Error 404, no maintenance list found for this factory", code=404)
        return queryset



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

# @api_view(['GET'])
# def get_active_check_warranty(request, sku):
#     try:
#         check_warranty = CheckWarranty.objects.get(product_id__sku=sku, is_active=True)
#         serializer = CheckWarrantySerializer(check_warranty)
#         return Response(serializer.data)
#     except CheckWarranty.DoesNotExist:
#         return Response({"message": "No active warranty found."}, status=200)

# api to check maintainence availible or not



# @api_view(['GET'])
# def get_active_check_maintenance(request, sku):
#     try:
#         check_maintenance = CheckMaintenance.objects.get(product_id__sku=sku, is_active=True)
#         serializer = CheckMaintenanceSerializer(check_maintenance)
#         return Response(serializer.data)
#     except :
#         return Response({"message": "No active  maintenance found ."}, status=200)
# api to create maintainence


# @api_view(['POST'])
# def create_maintenance(request):
#     data = request.data
#     serializer = MaintenanceSerializer(data=data)
#     if serializer.is_valid():
#         check_maintenance = serializer.validated_data.get('maintanence_id')
#         check_maintenance_id = check_maintenance.id if check_maintenance else None
#         print(check_maintenance_id)  # Print the value for debugging
#         if check_maintenance_id is not None:
#             CheckMaintenance.objects.filter(id=check_maintenance_id).update(is_active=False)
#         mentain = serializer.save()
#         parts = data.get("replace_parts","").split(",")

#         for i in parts:
#             mentain.replace_parts.add(newSparePart.objects.get(id=int(i)))

#         mentain.save()

#         return Response(serializer.data, status=201)
#     else:
#         return Response(serializer.errors, status=400)

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
# class SparePartList(generics.ListCreateAPIView):
#     queryset = SparePart.objects.all()
#     serializer_class = SparePartSerializer

# class SparePartDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = SparePart.objects.all()
#     serializer_class = SparePartSerializer

@api_view(['GET'])
def get_product_by_vin(request, vin_code):
    try:
        product = Product.objects.get(vin_code=vin_code)
        serializer = getProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({'message': 'Product not found'}, status=404)

# @api_view(['POST'])
# def add_service(request):
#     serializer = addServiceSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_services(request):
#     services = Maintainence_panel.objects.all()
#     serializer = addServiceSerializer(Maintainence_panel, many=True)
#     return Response(serializer.data)

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




# @api_view(['POST'])
# def create_history(request):
#     serializer = HistorySerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         message = {'message': 'History instance created successfully.'}
#         response_data = {**serializer.data, **message}
#         return Response(response_data, status=201)
#     return Response(serializer.errors, status=400)

# @api_view(['GET'])
# def get_history_by_product(request, product_id):
#     try:
#         history = History.objects.filter(product_id=product_id).order_by('timestamp')
#         serializer = HistorySerializer(history, many=True)
#         return Response(serializer.data, status=200)
#     except History.DoesNotExist:
#         message = {'error': f'No history available for product with id {product_id}.'}
#         return Response(message, status=404)
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

class ProductServiceCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ProductServiceSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
