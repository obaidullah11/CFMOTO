from django.urls import path
from .views import*
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('product/vin/<str:vin_code>/', get_product_by_vin, name='get_product_by_vin'),
    # path('products/create/', create_product_dealer, name='create-product'),
    # path('products/<int:pk>/update/', release_product_from_factory, name='update-product'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)