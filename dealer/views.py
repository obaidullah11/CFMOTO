# from django.shortcuts import render


# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from products.models import Product
# from .models import *
# from .serializers import ProductnewSerializer, HistorySerializer


# @api_view(['POST'])
# def create_product_dealer(request):
#     serializer = ProductnewSerializer(data=request.data)
#     print("============",serializer)
#     if serializer.is_valid():
#         product = serializer.save()
#         history = History(product=product, description="Product created")
#         history_serializer = HistorySerializer(history)
#         history_serializer.is_valid()
#         history_serializer.save()
#         response_data = {
#             'message': 'Product created successfully',
#             'product': serializer.data
#         }
#         return Response(response_data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['PUT'])
# def release_product_from_factory(request, pk):
#     try:
#         product = Product.objects.get(pk=pk)
#     except Product.DoesNotExist:
#         return Response({'message': 'Product does not exist'}, status=status.HTTP_404_NOT_FOUND)

#     request.data['vin_code'] = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=17))

#     serializer = ProductSerializer(product, data=request.data, partial=True)
#     if serializer.is_valid():
#         updated_product = serializer.save()
#         history = History(product=updated_product, description="Product updated")
#         history_serializer = HistorySerializer(history)
#         history_serializer.is_valid()
#         history_serializer.save()
#         response_data = {
#             'message': 'Product shiped from factory',
#             'vin_code': vin_code,
#             'product': serializer.data
#         }
#         return Response(response_data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)