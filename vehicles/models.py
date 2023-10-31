from django.db import models
from django.utils import timezone
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name
    
class SKU(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='SKU_category', default=None, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "SKU"
class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Manufacturer_category', default=None, blank=True, null=True)

    def __str__(self):
        return self.name
# from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Country_category', default=None, blank=True, null=True)
    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Series_category', default=None, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Series"





class Color(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Color_category', default=None, blank=True, null=True)
    def __str__(self):
        return self.name


class EUTypeApproval(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='EUTypeApproval_category', default=None, blank=True, null=True)
    def __str__(self):
        return self.name


# class BodyType(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.name


class SteeringPower(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='SteeringPower_category', default=None, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Steering Power"


class Wheels(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Wheels_category', default=None, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Wheels"


class Screen(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Screen_category', default=None, blank=True, null=True)

    def __str__(self):
        return self.name
class Factory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Factory_category', default=None, blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Factory name"    

class Lights(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Lights_category', default=None, blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Lights"
class CargoCompartment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()  # Adding a description field
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='CargoCompartment_category', default=None, blank=True, null=True)
    # Add other fields specific to the CargoCompartment model

    def __str__(self):
        return self.name

class CommunicationTerminal(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='CommunicationTerminal_category', default=None, blank=True, null=True)
    
      # Adding a description field
      
      
    # Add other fields specific to the CommunicationTerminal model

    def __str__(self):
        return self.name


class ModelName(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='ModelName_category', default=None, blank=True, null=True)
    # factory_name = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='Factory_modelname', default=None, blank=True, null=True)
    def __str__(self):
        return self.name
class EUTypeApproval(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='EUTypeApproval_category', default=None, blank=True, null=True)
    # factory_name = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='Factory_eutype', default=None, blank=True, null=True)
    def __str__(self):
        return self.name    
class Vehicle(models.Model):
    Manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, blank=True, null=True)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, blank=True, null=True)
    Factory_name = models.ForeignKey(Factory, on_delete=models.CASCADE, blank=True, null=True)
    model_name = models.ForeignKey(ModelName, on_delete=models.CASCADE, blank=True, null=True)
    eu_type = models.ForeignKey(EUTypeApproval, on_delete=models.CASCADE, blank=True, null=True)
    steering_power = models.ForeignKey(SteeringPower, on_delete=models.CASCADE, blank=True, null=True)
    wheels = models.ForeignKey(Wheels, on_delete=models.CASCADE, blank=True, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    lights = models.ForeignKey(Lights, on_delete=models.CASCADE, blank=True, null=True)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, blank=True, null=True)
    cargo_compartment = models.ForeignKey(CargoCompartment, on_delete=models.CASCADE, blank=True, null=True)
    communication_terminal = models.ForeignKey(CommunicationTerminal, on_delete=models.CASCADE, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE, blank=True, null=True)
    orderer_email = models.EmailField(blank=True, null=True)
    orderer_name = models.CharField(max_length=100,blank=True, null=True)
    orderer_phone = models.CharField(max_length=15,blank=True, null=True)

    
    def __str__(self):
        
        return f"{self.Factory_name} - {self.series} - {self.model_name}"
class ProductImage(models.Model):
    product = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    # Add other fields if needed (e.g., image title, description, etc.)

    def __str__(self):
        return f"{self.product.sku} - Image {self.pk}"
    

    class Meta:
        verbose_name_plural = "Vehicle Images"


