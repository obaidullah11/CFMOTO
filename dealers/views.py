from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import RegisteredVehicle
from .serializers import RegisteredVehicleSerializer

# @api_view(['GET'])
# def get_product_by_vin(request):
#     vin_code = request.data.get('vin_code', None)

#     if vin_code is not None:
#         queryset = RegisteredVehicle.objects.filter(received_vehicle__vin_code=vin_code)
#         serializer = RegisteredVehicleSerializer(queryset, many=True)
#         return Response(serializer.data)
#     else:
#         return Response({'error': 'Please provide a VIN code in the request body.'}, status=400)
    
@api_view(['GET'])
def get_product_by_vin(request, vin_code):
    try:
        product = RegisteredVehicle.objects.get(vin_code=vin_code)
        serializer = RegisteredVehicleSerializer(product)
        return Response(serializer.data)
    except product.DoesNotExist:
        return Response({'message': 'Product not found'}, status=404)