from django.db import models
from django.utils import timezone
import random
import string
from users.models import User
from sortedm2m.fields import SortedManyToManyField
from dealers.models import RegisteredVehicle
from vehicles.models import Factory,SKU,Series

from datetime import datetime
from django_toggle_m2m.toggle import ToggleManyToMany
class Vincode(models.Model):
    vincode = models.CharField(max_length=17, unique=True)


    # You can add more fields as needed

    def __str__(self):
        return self.vincode
class Year(models.Model):
    Year = models.CharField(max_length=255)

    def __str__(self):
        return self.Year
class Bulletins(models.Model):
    bulletins_name = models.CharField(max_length=100)
    bulletins_description = models.TextField( blank=True)
    pdf_instructions = models.FileField(upload_to='pdf_instructions/')
    Date = models.DateTimeField(default=datetime.now)
   
    series = models.ManyToManyField(Series,)
    years = models.ManyToManyField(Year, blank=True)
    factoryname = models.ManyToManyField(Factory,)
    vincode = models.ManyToManyField('Vincode', blank=True)
    


    def __str__(self):
        return self.bulletins_name
    class Meta:
        verbose_name = 'Bulletins'
        verbose_name_plural = 'Bulletins'
class Vehicle(models.Model):
    MODEL_SKU = models.CharField(max_length=50, null=True)
    CATEGORY = models.CharField(max_length=50, null=True)
    MODEL_NAME = models.CharField(max_length=50, null=True)
    FACTORY = models.CharField(max_length=50, null=True)
    SERIES = models.CharField(max_length=50, null=True)
    FACTORY_NAME = models.CharField(max_length=50, null=True)
    COLOR = models.CharField(max_length=50, null=True)
    EU_TYPE = models.CharField(max_length=50, null=True)
    WHEELS = models.CharField(max_length=50,null=True)
    STEERING = models.CharField(max_length=50, null=True)
    SCREEN = models.CharField(max_length=50, null=True)
    LIGHTS = models.CharField(max_length=50, null=True)
    CARGO_COMPARTMENTS = models.CharField(max_length=50, null=True)
    COMMUNICATION_TERMINAL = models.CharField(max_length=50, null=True)
    vehicle_system_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        if self.MODEL_NAME is None:
            return "No model name available"
        return str(self.MODEL_NAME)

    def save(self, *args, **kwargs):
        if not self.vehicle_system_id:
            last_product = Vehicle.objects.order_by('-vehicle_system_id').first()
            if last_product:
                last_system_id = last_product.vehicle_system_id.split('-')[1]
                new_system_id = str(int(last_system_id) + 1).zfill(4)
            else:
                new_system_id = '0001'
            self.vehicle_system_id = '1000-' + new_system_id
        super().save(*args, **kwargs)



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
class Product(models.Model):
    sku = models.CharField(max_length=50,blank=True)
    vin_code = models.CharField(max_length=50,blank=True)
    manufacture = models.CharField(max_length=100, null=True,blank=True)
    country = models.CharField(max_length=100, null=True,blank=True)
    series = models.CharField(max_length=100, null=True,blank=True)
    model_name = models.CharField(max_length=100, null=True,blank=True)
    factory_name = models.CharField(max_length=100, null=True,blank=True)
    color = models.CharField(max_length=50, null=True,blank=True)
    eu_type_approval = models.CharField(max_length=50, null=True,blank=True)
    body_type = models.CharField(max_length=50, null=True,blank=True)
    steering_power = models.CharField(max_length=50, null=True,blank=True)
    wheels = models.CharField(max_length=50, null=True,blank=True)
    screen = models.CharField(max_length=50, null=True,blank=True)
    lights = models.CharField(max_length=50, null=True,blank=True)
    cargo_compartments = models.CharField(max_length=50, null=True,blank=True)
    communication_terminal = models.CharField(max_length=50, null=True,blank=True)
    date_of_manufacture = models.DateField(null=True,blank=True)
    orderer = models.CharField(max_length=100, null=True,blank=True)
    orderer_phone = models.CharField(max_length=50, null=True,blank=True)
    orderer_email = models.EmailField(null=True,blank=True)
    importer = models.CharField(max_length=100, null=True,blank=True)
    dealer = models.CharField(max_length=100, null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True,blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    public_id = models.IntegerField(null=True)

    def __str__(self):
        return self.model_name
    class Meta:
        verbose_name = 'Registered vehicles'
        verbose_name_plural = 'Registered vehicles'
class newSparePart(models.Model):
    product = models.ForeignKey(RegisteredVehicle, on_delete=models.CASCADE)
    model_id = models.CharField(max_length=100)
    id_code = models.CharField(max_length=100)
    part_name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return f"{self.product.sku} - {self.product.sku}"

class Mileage(models.Model):
    Mileage = models.CharField(max_length=255)

    def __str__(self):
        return self.Mileage
class Maintainencepoint(models.Model):
    Point_id = models.AutoField(primary_key=True, db_column='id')
    # Maintenance_List_Point = models.ForeignKey(Service, on_delete=models.CASCADE)
    Maintainencepoint_name =models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    instruction_active = models.BooleanField(default=False)
    fill_active = models.BooleanField(default=False)
    value_active = models.BooleanField(default=False)


    image_1 = models.ImageField(upload_to='service_images/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='service_images/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='service_images/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='service_images/', blank=True, null=True)
    image_5 = models.ImageField(upload_to='service_images/', blank=True, null=True)

    video1 = models.URLField(blank=True, null=True)
    video2 = models.URLField(blank=True, null=True)
    video3 = models.URLField(blank=True, null=True)
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True
    )


    def __str__(self):
        return str(self.Maintainencepoint_name)
    class Meta:
        ordering = ['my_order']
        verbose_name_plural = "Maintenance points"
class Maintenance_List(models.Model):
    Maintenance_list_id = models.AutoField(primary_key=True, db_column='id')
    Maintenance_list_name = models.CharField(max_length=100)
    Maintainence_description = models.TextField(blank=True, null=True)
    Maintenance_List_Point_name = SortedManyToManyField(Maintainencepoint,sorted="my_order")
    # Maintenance_List_Point_name = models.ManyToManyField(Maintainencepoint)
    mileage = models.ManyToManyField(Mileage)
    Year = models.ManyToManyField(Year)
    Factory_name = models.ManyToManyField(Factory)
    # SKU = models.ManyToManyField(SKU)


    # my_order = models.PositiveIntegerField(
    #     default=0,
    #     blank=False,
    #     null=False,
    #     db_index=True
    # )

    def __str__(self):
        return self.Maintenance_list_name
    class Meta:

        verbose_name = "Maintenance List"
        verbose_name_plural = "Maintenance Lists"



class ServiceImage(models.Model):
    product = models.ForeignKey(RegisteredVehicle, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='service_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='service_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='service_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='service_images/', null=True, blank=True)

    def __str__(self):
        return f"ServiceImage {self.id} for {self.product.id}"

class ProductService(models.Model):
    is_active = models.BooleanField(default=True)
    comment = models.TextField(null=True, blank=True)
    executed = models.BooleanField(default=False)
    fill = models.CharField(max_length=50, null=True, blank=True)
    value = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    product = models.ForeignKey(RegisteredVehicle, on_delete=models.CASCADE, related_name='services', null=True)
    name = models.CharField(max_length=100)
    time_spent = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return f"{self.name} - {self.product.sku}"
    class Meta:
        verbose_name = 'Maintenance preparation'
        verbose_name_plural = 'Maintenance preparation'


class MechanicalNote(models.Model):
    product = models.ForeignKey(RegisteredVehicle, on_delete=models.CASCADE, related_name='mechanical_notes')
    note = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.date_created}"
class ProductService(models.Model):
    is_active = models.BooleanField(default=True)
    comment = models.TextField(null=True, blank=True)
    executed = models.BooleanField(default=False)
    fill = models.CharField(max_length=50, null=True, blank=True)
    value = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    product = models.ForeignKey(RegisteredVehicle, on_delete=models.CASCADE, related_name='services', null=True)
    name = models.CharField(max_length=100)
    time_spent = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services')

    def __str__(self):
        return f"{self.name} - {self.product.sku}"
    class Meta:
        verbose_name = 'Maintenance preparation'
        verbose_name_plural = 'Maintenance preparation'


class MechanicalNote(models.Model):
    product = models.ForeignKey(RegisteredVehicle, on_delete=models.CASCADE, related_name='mechanical_notes')
    note = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} - {self.date_created}"
class CheckWarranty(models.Model):
    product_id = models.ForeignKey(RegisteredVehicle, on_delete=models.CASCADE)
    warranty_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product_id.sku} - {self.warranty_name}"

    def save(self, *args, **kwargs):
        if self.is_active:
            # Deactivate all other records with is_active=True except self
            CheckWarranty.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
        super().save(*args, **kwargs)
class Repairing(models.Model):
    product_id = models.ForeignKey(RegisteredVehicle, on_delete=models.CASCADE)
    mileage = models.PositiveIntegerField()
    customer_description = models.TextField()
    receiver_description = models.TextField()
    feedback = models.TextField()
    replace_parts = models.ManyToManyField(newSparePart)
    picture = models.ImageField(upload_to='maintenance/', null=True)
    video = models.FileField(upload_to='maintenance/', null=True)
    time = models.CharField("Time", max_length=255)
    repairing_id = models.CharField("Repairing ID", max_length=9, unique=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.repairing_id:
            last_repairing = Repairing.objects.order_by('-id').first()
            if last_repairing:
                last_id = int(last_repairing.repairing_id.split('-')[1])
                new_id = f"{last_repairing.repairing_id.split('-')[0]}-{str(last_id + 1).zfill(4)}"
            else:
                new_id = "4000-0001"
            self.repairing_id = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_id.sku} - {self.product_id.sku}"



class Warranty(models.Model):
    product_id = models.ForeignKey(RegisteredVehicle, on_delete=models.CASCADE)
    mileage = models.PositiveIntegerField()
    cause = models.TextField()
    review = models.TextField()
    remarks = models.TextField()
    failure_description = models.TextField()
    replace_parts = models.ManyToManyField(newSparePart)
    picture = models.ImageField(upload_to='maintenance/', null=True)
    video = models.FileField(upload_to='maintenance/', null=True)
    time = models.CharField("Time", max_length=255)
    Warranty_id = models.CharField("Warranty ID", max_length=9, unique=True)

    def save(self, *args, **kwargs):
        if not self.id and not self.Warranty_id:
            last_repairing = Warranty.objects.order_by('-id').first()
            if last_repairing:
                last_id = int(last_repairing.Warranty_id.split('-')[1])
                new_id = f"{last_repairing.Warranty_id.split('-')[0]}-{str(last_id + 1).zfill(4)}"
            else:
                new_id = "6000-0001"
            self.Warranty_id = new_id
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_id.sku} - {self.product_id.sku}"
