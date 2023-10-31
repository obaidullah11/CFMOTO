# from django.db import models
# from django.utils import timezone
# import random
# import string
# from users.models import User
# from sortedm2m.fields import SortedManyToManyField
# from dealers.models import RegisteredVehicle
# from vehicles.models import Factory,SKU
# from django_toggle_m2m.toggle import ToggleManyToMany

# # class Vehicle(models.Model):
# #     MODEL_SKU = models.CharField(max_length=50, null=True)
# #     CATEGORY = models.CharField(max_length=50, null=True)
# #     MODEL_NAME = models.CharField(max_length=50, null=True)
# #     FACTORY = models.CharField(max_length=50, null=True)
# #     SERIES = models.CharField(max_length=50, null=True)
# #     FACTORY_NAME = models.CharField(max_length=50, null=True)
# #     COLOR = models.CharField(max_length=50, null=True)
# #     EU_TYPE = models.CharField(max_length=50, null=True)
# #     WHEELS = models.CharField(max_length=50,null=True)
# #     STEERING = models.CharField(max_length=50, null=True)
# #     SCREEN = models.CharField(max_length=50, null=True)
# #     LIGHTS = models.CharField(max_length=50, null=True)
# #     CARGO_COMPARTMENTS = models.CharField(max_length=50, null=True)
# #     COMMUNICATION_TERMINAL = models.CharField(max_length=50, null=True)
# #     vehicle_system_id = models.CharField(max_length=50, unique=True)

# #     def __str__(self):
# #         if self.MODEL_NAME is None:
# #             return "No model name available"
# #         return str(self.MODEL_NAME)

# #     def save(self, *args, **kwargs):
# #         if not self.vehicle_system_id:
# #             last_product = Vehicle.objects.order_by('-vehicle_system_id').first()
# #             if last_product:
# #                 last_system_id = last_product.vehicle_system_id.split('-')[1]
# #                 new_system_id = str(int(last_system_id) + 1).zfill(4)
# #             else:
# #                 new_system_id = '0001'
# #             self.vehicle_system_id = '1000-' + new_system_id
# #         super().save(*args, **kwargs)


# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

#     def __str__(self):
#         return self.name
# class Subcategory(models.Model):
#     name = models.CharField(max_length=100)
#     parent = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

#     def __str__(self):
#         return self.name

# # class Product(models.Model):
# #     sku = models.CharField(max_length=50,blank=True)
# #     vin_code = models.CharField(max_length=50,blank=True)
# #     manufacture = models.CharField(max_length=100, null=True,blank=True)
# #     country = models.CharField(max_length=100, null=True,blank=True)
# #     series = models.CharField(max_length=100, null=True,blank=True)
# #     model_name = models.CharField(max_length=100, null=True,blank=True)
# #     factory_name = models.CharField(max_length=100, null=True,blank=True)
# #     color = models.CharField(max_length=50, null=True,blank=True)
# #     eu_type_approval = models.CharField(max_length=50, null=True,blank=True)
# #     body_type = models.CharField(max_length=50, null=True,blank=True)
# #     steering_power = models.CharField(max_length=50, null=True,blank=True)
# #     wheels = models.CharField(max_length=50, null=True,blank=True)
# #     screen = models.CharField(max_length=50, null=True,blank=True)
# #     lights = models.CharField(max_length=50, null=True,blank=True)
# #     cargo_compartments = models.CharField(max_length=50, null=True,blank=True)
# #     communication_terminal = models.CharField(max_length=50, null=True,blank=True)
# #     date_of_manufacture = models.DateField(null=True,blank=True)
# #     orderer = models.CharField(max_length=100, null=True,blank=True)
# #     orderer_phone = models.CharField(max_length=50, null=True,blank=True)
# #     orderer_email = models.EmailField(null=True,blank=True)
# #     importer = models.CharField(max_length=100, null=True,blank=True)
# #     dealer = models.CharField(max_length=100, null=True,blank=True)
# #     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True,blank=True)
# #     image = models.ImageField(upload_to='product_images/', null=True, blank=True)
# #     public_id = models.IntegerField(null=True)

# #     def __str__(self):
# #         return self.model_name
# #     class Meta:
# #         verbose_name = 'Registered vehicles'
# #         verbose_name_plural = 'Registered vehicles'

# # class newSparePart(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     model_id = models.CharField(max_length=100)
# #     id_code = models.CharField(max_length=100)
# #     part_name = models.CharField(max_length=100)
# #     description = models.TextField()
# #     def __str__(self):
# #         return f"{self.product.sku} - {self.product.sku}"

# # class Product(models.Model):
# #     sku = models.CharField(max_length=50, unique=True, editable=False, null=True)
# #     vin_code = models.CharField(max_length=50, null=True, unique=True)
# #     manufacture = models.CharField(max_length=100, null=True)
# #     country = models.CharField(max_length=100, null=True)
# #     series = models.CharField(max_length=100, null=True)
# #     model_name = models.CharField(max_length=100, null=True)
# #     factory_name = models.CharField(max_length=100, null=True)
# #     color = models.CharField(max_length=50, null=True)
# #     eu_type_approval = models.CharField(max_length=50, null=True)
# #     body_type = models.CharField(max_length=50, null=True)
# #     steering_power = models.CharField(max_length=50, null=True)
# #     wheels = models.CharField(max_length=50, null=True)
# #     screen = models.CharField(max_length=50, null=True)
# #     lights = models.CharField(max_length=50, null=True)
# #     cargo_compartments = models.CharField(max_length=50, null=True)
# #     communication_terminal = models.CharField(max_length=50, null=True)
# #     date_of_manufacture = models.DateField(null=True)
# #     orderer = models.CharField(max_length=100, null=True)
# #     orderer_phone = models.CharField(max_length=50, null=True)
# #     orderer_email = models.EmailField(null=True)
# #     importer = models.CharField(max_length=100, null=True)
# #     dealer = models.CharField(max_length=100, null=True)
# #     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
# #     sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products', null=True)
# #     image = models.ImageField(upload_to='product_images/', null=True, blank=True)


# #     def save(self, *args, **kwargs):
# #         if not self.sku:
# #             # generate a random 6-digit SKU
# #             while True:
# #                 sku = ''.join(random.choices('0123456789', k=6))
# #                 if not Product.objects.filter(sku=sku).exists():
# #                     break
# #             self.sku = sku

# #         if not self.vin_code:
# #             # generate a random 17-character VIN code
# #             while True:
# #                 vin_code = ''.join(random.choices(string.ascii_uppercase + '0123456789', k=17))
# #                 if not Product.objects.filter(vin_code=vin_code).exists():
# #                     break
# #             self.vin_code = vin_code

# #         super().save(*args, **kwargs)


# class SparePart(models.Model):
#     model_id = models.CharField(max_length=100)
#     id_code = models.CharField(max_length=100)
#     part_name = models.CharField(max_length=100)
#     description = models.TextField()
#     def __str__(self):
#         return self.part_name
# # class History(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='history')
# #     timestamp = models.DateTimeField(auto_now_add=True)
# #     description = models.CharField(max_length=255)

# #     class Meta:
# #         ordering = ['-timestamp']
# # 333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333
# class Year(models.Model):
#     Year = models.CharField(max_length=255)

#     def __str__(self):
#         return self.Year
# # class Year(models.Model):
# #     year = models.CharField(unique=True,max_length=255,blank=True, null=True)

# #     def __str__(self):
# #         return str(self.year)
# class Mileage(models.Model):
#     Mileage = models.CharField(max_length=255)

#     def __str__(self):
#         return self.Mileage
# # class Mileage(models.Model):
# #     value = models.CharField(max_length=255,blank=True, null=True)

# #     def __str__(self):
# #         return str(self.value)


# # class MaintenanceListPoint(models.Model):
# #     Maintenance_List_Point_name = models.CharField(max_length=100)
# #     # maintenance_points = models.ManyToManyField(Maintainencepoint, related_name='maintenance_lists')
# #     my_order = models.PositiveIntegerField(
# #         default=0,
# #         blank=False,
# #         null=False,
# #         db_index=True
# #     )

# #     def __str__(self):
# #         return self.Maintenance_List_Point_name
# #     class Meta:
# #         ordering = ['my_order']
# #         # verbose_name_plural = "Maintenance points"


# # class Service(models.Model):
# #     Maintenance_list_name = models.CharField(max_length=100)
# #     Maintainence_description = models.TextField(blank=True, null=True)
# #     Maintainencepoint = models.ForeignKey(Maintainencepoint, on_delete=models.CASCADE)
# #     mileage = models.ForeignKey(Mileage, on_delete=models.CASCADE)
# #     Year = models.ForeignKey(Year, on_delete=models.CASCADE)
# #     Factory_name=  models.ForeignKey(Factory, on_delete=models.CASCADE)
# #     SKU=  models.ForeignKey(SKU, on_delete=models.CASCADE)
# #     # instructions = models.TextField(blank=True, null=True)

# #     # instruction_active = models.BooleanField(default=False)
# #     # fill_active = models.BooleanField(default=False)
# #     # value_active = models.BooleanField(default=False)


# #     # image_1 = models.ImageField(upload_to='service_images/', blank=True, null=True)
# #     # image_2 = models.ImageField(upload_to='service_images/', blank=True, null=True)
# #     # image_3 = models.ImageField(upload_to='service_images/', blank=True, null=True)
# #     # image_4 = models.ImageField(upload_to='service_images/', blank=True, null=True)

# #     # video = models.URLField(blank=True, null=True)
# #     my_order = models.PositiveIntegerField(
# #         default=0,
# #         blank=False,
# #         null=False,
# #         db_index=True
# #     )


# #     def __str__(self):
# #         return self.name
# #     class Meta:
# #         ordering = ['my_order']
# #         verbose_name = "Maintenance List"
# #         verbose_name_plural = "Maintenance list"
# class Maintainencepoint(models.Model):
#     Point_id = models.AutoField(primary_key=True, db_column='id')
#     # Maintenance_List_Point = models.ForeignKey(Service, on_delete=models.CASCADE)
#     Maintainencepoint_name =models.TextField(blank=True, null=True)
#     instructions = models.TextField(blank=True, null=True)
#     instruction_active = models.BooleanField(default=False)
#     fill_active = models.BooleanField(default=False)
#     value_active = models.BooleanField(default=False)


#     image_1 = models.ImageField(upload_to='service_images/', blank=True, null=True)
#     image_2 = models.ImageField(upload_to='service_images/', blank=True, null=True)
#     image_3 = models.ImageField(upload_to='service_images/', blank=True, null=True)
#     image_4 = models.ImageField(upload_to='service_images/', blank=True, null=True)

#     video = models.URLField(blank=True, null=True)
#     my_order = models.PositiveIntegerField(
#         default=0,
#         blank=False,
#         null=False,
#         db_index=True
#     )


#     def __str__(self):
#         return str(self.Maintainencepoint_name)
#     class Meta:
#         ordering = ['my_order']
#         verbose_name_plural = "Maintenance points"
#     # def youtube_link(self):
#     # if self.video:
#     #     video_id = extract_video_id(self.video)  # Function to extract video ID from URL
#     #     youtube_url = f"https://www.youtube.com/watch?v={video_id}"
#     #     return format_html('<a href="{}" target="_blank">YouTube Link</a>', youtube_url)
#     # return ''



# class Maintenance_List(models.Model):
#     Maintenance_list_id = models.AutoField(primary_key=True, db_column='id')
#     Maintenance_list_name = models.CharField(max_length=100)
#     Maintainence_description = models.TextField(blank=True, null=True)
#     Maintenance_List_Point_name = models.ManyToManyField(Maintainencepoint)
#     mileage = models.ManyToManyField(Mileage)
#     Year = models.ManyToManyField(Year)
#     Factory_name = models.ManyToManyField(Factory)
#     # SKU = models.ManyToManyField(SKU)


#     my_order = models.PositiveIntegerField(
#         default=0,
#         blank=False,
#         null=False,
#         db_index=True
#     )

#     def __str__(self):
#         return self.Maintenance_list_name
#     # TOGGLEABLE_FIELDS = ('my_order',)
#     class Meta:
#         ordering = ['my_order']
#         verbose_name = "Maintenance List"
#         verbose_name_plural = "Maintenance Lists"

# # class MaintenancePointOrder(models.Model):
# #     maintenance_list_name = models.CharField(max_length=100)
# #     maintenance_point_name = models.CharField(max_length=100)
# #     order = models.PositiveIntegerField()

# #     def __str__(self):
# #         return f"{self.maintenance_list_name} - {self.maintenance_point_name}"

# # class  Maintainence_panel(models.Model):
# #     name = models.CharField(max_length=100)
# #     instructions = models.TextField(blank=True, null=True)
# #     instruction_active = models.BooleanField(default=False)
# #     fill_active = models.BooleanField(default=False)
# #     value_active = models.BooleanField(default=False)
# #     image_1 = models.ImageField(upload_to='service_images/', blank=True, null=True)
# #     image_2 = models.ImageField(upload_to='service_images/', blank=True, null=True)
# #     image_3 = models.ImageField(upload_to='service_images/', blank=True, null=True)
# #     image_4 = models.ImageField(upload_to='service_images/', blank=True, null=True)
# #     video = models.URLField(blank=True, null=True)
# #     def __str__(self):
# #         return self.name



# # class ServiceImage(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     image1 = models.ImageField(upload_to='service_images/', null=True, blank=True)
# #     image2 = models.ImageField(upload_to='service_images/', null=True, blank=True)
# #     image3 = models.ImageField(upload_to='service_images/', null=True, blank=True)
# #     image4 = models.ImageField(upload_to='service_images/', null=True, blank=True)

# #     def __str__(self):
# #         return f"ServiceImage {self.id} for {self.product.sku}"





# # class SubService(models.Model):
# #     service = models.ForeignKey(Service, on_delete=models.CASCADE)
# #     is_active = models.BooleanField(default=True)
# #     comment = models.TextField(null=True, blank=True)
# #     executed = models.BooleanField(default=False)
# #     fill = models.CharField(max_length=50, null=True, blank=True)
# #     value = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

# #     def __str__(self):
# #         return f"{self.service} - {self.fill}"




# # 333333333333333333333333333333333333333333333333333333333333333333333
# # class ProductService(models.Model):
# #     is_active = models.BooleanField(default=True)
# #     comment = models.TextField(null=True, blank=True)
# #     executed = models.BooleanField(default=False)
# #     fill = models.CharField(max_length=50, null=True, blank=True)
# #     value = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='services', null=True)
# #     name = models.CharField(max_length=100)
# #     time_spent = models.IntegerField(null=True, blank=True)
# #     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services')

# #     def __str__(self):
# #         return f"{self.name} - {self.product.sku}"
# #     class Meta:
# #         verbose_name = 'Maintenance preparation'
# #         verbose_name_plural = 'Maintenance preparation'


# # class MechanicalNote(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='mechanical_notes')
# #     note = models.TextField()
# #     date_created = models.DateTimeField(auto_now_add=True)

#     # def __str__(self):
#     #     return f"{self.product} - {self.date_created}"


# # HISTORICAL_CHOICES = (
# #         ('The vehicle order has been forwarded to the factory.', 'The vehicle order has been forwarded to the factory.'),

# #         ('The vehicle is out of production.', 'The vehicle is out of production.'),
# #         ('The vehicle is ready for transport from the factory.', 'The vehicle is ready for transport from the factory.'),
# #         ('The vehicle arrived at the MOTOHOBI warehouse.', 'The vehicle arrived at the MOTOHOBI warehouse.'),
# #         ('The vehicle has been transferred to the dealer.', 'The vehicle has been transferred to the dealer.'),
# #         ('The vehicle is registered and issued with a reg number', 'The vehicle is registered and issued with a reg number'),
# #         # ('The vehicle is registered and issued with a reg number', 'The vehicle is registered and issued with a reg number'),
# #         ('The vehicle has been issued to the owner.', 'The vehicle has been issued to the owner.'),

# #     )

# # class History(models.Model):
# #     timestamp = models.DateTimeField(default=timezone.now)
# #     description = models.CharField(max_length=200)
# #     historical_note=models.CharField(max_length=150, choices=HISTORICAL_CHOICES)
# #     VIN_code = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

# #     def __str__(self):
#         # return f"{self.timestamp} - {self.description} - Product: {self.VIN_code.sku}"



# # class ProductTotalTime(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     service = models.ForeignKey(ProductService, on_delete=models.CASCADE)
# #     total_time_spent = models.DurationField(default=timezone.timedelta())

# #     def __str__(self):
# #         return f"{self.product.sku} - {self.service.name}"

# # class Maintenance(models.Model):
# #     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     mileage = models.PositiveIntegerField()
# #     customer_description = models.TextField()
# #     receiver_description = models.TextField()
# #     feedback = models.TextField()
# #     replace_part = models.BooleanField(default=False)
# #     picture = models.ImageField(upload_to='maintenance/', null=True)
# #     video = models.FileField(upload_to='maintenance/', null=True)

# #     def __str__(self):
# #         return f"{self.product_id.sku} - {self.product_id.sku}"


# # class WarrantyClaim(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     mileage = models.CharField(max_length=50)
# #     failure_description = models.TextField()
# #     repair_parts = models.TextField()
# #     cause = models.TextField()
# #     repair_remarks = models.TextField()
# #     review = models.TextField()
# #     remark = models.TextField(blank=True)
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     image = models.ImageField(upload_to='warranty_claims/images/', blank=True, null=True)
# #     video = models.FileField(upload_to='warranty_claims/videos', null=True)
# #     def __str__(self):
# #         return f"{self.product.sku} - {self.product.sku}"







# # new ###############################
# # class CheckMaintenance(models.Model):
# #     product_id = models.ForeignKey(RegisteredVehicle, on_delete=models.CASCADE)
# #     maintenance_name = models.CharField(max_length=255)
# #     is_active = models.BooleanField(default=False)

# #     def __str__(self):
# #         return f"{self.product_id.sku} - {self.maintenance_name}"

# #     def save(self, *args, **kwargs):
# #         if self.is_active:
# #             # Deactivate all other records with is_active=True except self
# #             CheckMaintenance.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
# #         super().save(*args, **kwargs)
# # class Maintenance(models.Model):

# #     maintanence_id = models.ForeignKey(CheckMaintenance,default=None, null=True, on_delete=models.CASCADE)
# #     product_id = models.ForeignKey(RegisteredVehicle, on_delete=models.CASCADE)
# #     mileage = models.PositiveIntegerField()
# #     customer_description = models.TextField()
# #     receiver_description = models.TextField()
# #     feedback = models.TextField()
# #     replace_parts = models.ManyToManyField(newSparePart)
# #     picture = models.ImageField(upload_to='maintenance/', null=True)
# #     video = models.FileField(upload_to='maintenance/', null=True)
# #     time = models.CharField("Time",max_length=255)
# #     def __str__(self):
# #         return f"{self.product_id.sku} - {self.product_id.sku}"

# # # new ###############################
# # class CheckWarranty(models.Model):
# #     product_id = models.ForeignKey(RegisteredVehicle, on_delete=models.CASCADE)
# #     warranty_name = models.CharField(max_length=255)
# #     is_active = models.BooleanField(default=False)

# #     def __str__(self):
# #         return f"{self.product_id.sku} - {self.warranty_name}"

# #     def save(self, *args, **kwargs):
# #         if self.is_active:
# #             # Deactivate all other records with is_active=True except self
# #             CheckWarranty.objects.filter(is_active=True).exclude(pk=self.pk).update(is_active=False)
# #         super().save(*args, **kwargs)
# # class Repairing(models.Model):
# #     product_id = models.ForeignKey(RegisteredVehicle, on_delete=models.CASCADE)
# #     mileage = models.PositiveIntegerField()
# #     customer_description = models.TextField()
# #     receiver_description = models.TextField()
# #     feedback = models.TextField()
# #     replace_parts = models.ManyToManyField(newSparePart)
# #     picture = models.ImageField(upload_to='maintenance/', null=True)
# #     video = models.FileField(upload_to='maintenance/', null=True)
# #     time = models.CharField("Time", max_length=255)
# #     repairing_id = models.CharField("Repairing ID", max_length=9, unique=True)

# #     def save(self, *args, **kwargs):
# #         if not self.id and not self.repairing_id:
# #             last_repairing = Repairing.objects.order_by('-id').first()
# #             if last_repairing:
# #                 last_id = int(last_repairing.repairing_id.split('-')[1])
# #                 new_id = f"{last_repairing.repairing_id.split('-')[0]}-{str(last_id + 1).zfill(4)}"
# #             else:
# #                 new_id = "4000-0001"
# #             self.repairing_id = new_id
# #         super().save(*args, **kwargs)

# #     def __str__(self):
# #         return f"{self.product_id.sku} - {self.product_id.sku}"



# # class Warranty(models.Model):
# #     product_id = models.ForeignKey(RegisteredVehicle, on_delete=models.CASCADE)
# #     mileage = models.PositiveIntegerField()
# #     cause = models.TextField()
# #     review = models.TextField()
# #     remarks = models.TextField()
# #     failure_description = models.TextField()
# #     replace_parts = models.ManyToManyField(newSparePart)
# #     picture = models.ImageField(upload_to='maintenance/', null=True)
# #     video = models.FileField(upload_to='maintenance/', null=True)
# #     time = models.CharField("Time", max_length=255)
# #     Warranty_id = models.CharField("Repairing ID", max_length=9, unique=True)

# #     def save(self, *args, **kwargs):
# #         if not self.id and not self.Warranty_id:
# #             last_repairing = Warranty.objects.order_by('-id').first()
# #             if last_repairing:
# #                 last_id = int(last_repairing.Warranty_id.split('-')[1])
# #                 new_id = f"{last_repairing.Warranty_id.split('-')[0]}-{str(last_id + 1).zfill(4)}"
# #             else:
# #                 new_id = "6000-0001"
# #             self.Warranty_id = new_id
# #         super().save(*args, **kwargs)

# #     def __str__(self):
# #         return f"{self.product_id.sku} - {self.product_id.sku}"
# # class Maintenance(models.Model):

# #     maintanence_id = models.ForeignKey(CheckMaintenance,default=None, null=True, on_delete=models.CASCADE)
# #     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     mileage = models.PositiveIntegerField()
# #     customer_description = models.TextField()
# #     receiver_description = models.TextField()
# #     feedback = models.TextField()
# #     replace_parts = models.ManyToManyField(newSparePart)
# #     picture = models.ImageField(upload_to='maintenance/', null=True)
# #     video = models.FileField(upload_to='maintenance/', null=True)
# #     time = models.CharField("Time",max_length=255)
# #     def __str__(self):
# #         return f"{self.product_id.sku} - {self.product_id.sku}"
