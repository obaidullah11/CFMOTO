from django.urls import path
# from .views import CategoryListCreateAPIView,SubcategoryList,MileageList,create_product,create_repairing,create_warranty,SubcategoryListView,SubcategoryDetailView,SubcategoryByParentView,SubcategoryCreateView,SparePartDetail,SparePartList,get_product_by_vin,add_service,get_services,mechanical_note_create,create_history,get_history_by_product,create_service_image,create_product_service,service_create,service_list,get_service_images,get_active_check_maintenance,get_active_check_warranty,create_maintenance,newsparepart_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # # path('create/category', CategoryListCreateAPIView.as_view(), name='category-list-create'),
    # # path('subcategories/', SubcategoryListView.as_view(), name='subcategory-list'),
    # # path('subcategories/<int:pk>/', SubcategoryDetailView.as_view(), name='subcategory-detail'),
    # # path('categories/<int:parent_id>/subcategories/', SubcategoryByParentView.as_view(), name='subcategory-by-parent'),
    # # path('products/create/', create_product, name='create_product'),
    # # path('subcategories/create/', SubcategoryCreateView.as_view(), name='subcategory-create'),
    # path('spareparts/', SparePartList.as_view(), name='sparepart_list'),
    # path('spareparts/<int:pk>/', SparePartDetail.as_view(), name='sparepart_detail'),
    # # path('product/vin/<str:vin_code>/', get_product_by_vin, name='get_product_by_vin'),
    # path('services/add/',add_service, name='add_service'),
    # path('getall/services/', get_services, name='service-list'),
    # path('product-service/create/', create_product_service, name='create_product_service'),
    # path('services/create/', service_create, name='service-create'),
    # # path('history/create/', create_history, name='create_history'),
    # # path('products/<int:product_id>/history/',get_history_by_product, name='get_history_by_product'),
    # path('service-image/', create_service_image, name='service-image'),
    # path('mechanical-notes/create/', mechanical_note_create, name='mechanical_note_create'),
    # path('getallservices/', service_list, name='service-list'),
    # path('api/maintenance/', create_maintenance, name='create_maintenance'),
    # # path('product-total-time/', create_product_total_time, name='create-product-total-time'),
    # # path('api/maintenance/', maintenance_list, name='maintenance-list'),
    # # path('api/maintenance/<int:pk>/', maintenance_detail, name='maintenance-detail'),
    # # # path('product-total-time/', create_product_total_time, name='create-product-total-time'),
    # # path('warranty-claims/', get_warranty_claims, name='warranty-claims-list'),
    # # path('warranty-claims/create/', create_warranty_claim, name='create-warranty-claim'),
    # # path('warranty-claims/update/<int:claim_id>/', update_warranty_claim, name='update-warranty-claim'),
    # path('api/service_image/<int:product_id>/', get_service_images, name='service-image-api'),
    # path('api/check_maintenance/<str:sku>/', get_active_check_maintenance, name='get_active_check_maintenance'),
    # path('api/check_warranty/<str:sku>/', get_active_check_warranty, name='get_active_check_warranty'),
    # path('api/newspareparts/<str:sku>/', newsparepart_detail, name='newsparepart-api'),
    # path('api/repairing/create/', create_repairing, name='create_repairing'),
    # path('api/warranty/create/', create_warranty, name='create_warranty'),
    #   # URL pattern for the ServiceList view, filtering by SKU and mileage
    # # path('services/<str:sku_name>/<int:target_mileage>/', ServiceList.as_view(), name='filter'),



    # path('mileages/', MileageList.as_view(), name='mileage-list'),


#


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)