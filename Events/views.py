# views.py
from rest_framework import generics
from rest_framework.response import Response
from .models import vehiclehystory
from .serializers import VehicleHistorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from .models import vehiclehystory
# from .serializers import VehicleHistorySerializer

class VehicleHistoryByVIN(generics.ListAPIView):
    serializer_class = VehicleHistorySerializer
    lookup_field = 'sku'

    def get_queryset(self):
        sku_str = self.kwargs['sku_str']  # Get the SKU from URL parameter
        return vehiclehystory.objects.filter(vehicle__sku__name=sku_str)
    





@api_view(['POST'])
def create_vehicle_history(request):
    if request.method == 'POST':
        serializer = VehicleHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
