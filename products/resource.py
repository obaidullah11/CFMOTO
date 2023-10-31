from import_export import resources 
from .models import Product
class ReportResource(resources.ModelResource):
     class Meta:
         model = Product