from django.urls import path
from .views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('products/<str:sku_str>/history/', VehicleHistoryByVIN.as_view(), name='vehicle-history-by-vin'),
    path('history/create/', create_vehicle_history),
    # path('products/create/', create_product_dealer, name='create-product'),
    # path('products/<int:pk>/update/', release_product_from_factory, name='update-product'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# urls.py
# from django.urls import path
# from .views import VehicleHistoryByVIN

# urlpatterns = [
#     path('products/<str:vincode>/history/', VehicleHistoryByVIN.as_view(), name='vehicle-history-by-vin'),
# ]
