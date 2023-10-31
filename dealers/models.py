from django.db import models
from users.models import User
from importer.models import DeliveredVehicle
from django.utils import timezone

# # from django.utils import timezone
# # from products.models import Product

# # class History(models.Model):
# #     timestamp = models.DateTimeField(default=timezone.now)
# #     description = models.CharField(max_length=200)
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)

# #     def __str__(self):
# #         # return f"{self.timestamp} - {self.description} - Product: {self.product.sku}"


# # class Order(models.Model):
# #     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)




# #     STATUS_CHOICES = (
# #         ('PN', 'pending '),
# #         ('RC', 'recieved '),

# #         ('AR', 'Assaign registration number'),
# #         ('DU', 'deliverd to user'),

# #     )
# #     status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='PN')

# #     def __str__(self):
# #         return f"Order ID: {self.pk} - {self.vehicle}"











class receivedvehicle(models.Model):
    manufacturing_date = models.DateTimeField(default=timezone.now)
    vin_code = models.CharField(max_length=17,null=True)
    vehicle = models.ForeignKey(DeliveredVehicle, on_delete=models.CASCADE)
    registration_number=models.CharField(max_length=17,null=True)

    STATUS_CHOICES = (
        ('PN', 'pending'),
        ('RC', 'received'),
        ('AR', 'Assign registration number'),
        # ('DU', 'delivered to user'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PN')
    name_received_product = models.CharField(max_length=100)


    def save(self, *args, **kwargs):
        # If the status is 'RC', set the name_received_product field to 'Factory'
        if self.status == 'RC':
            self.name_received_product = 'Factory'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.manufacturing_date} - {self.vehicle} - {self.get_status_display()}"
    class Meta:
        verbose_name_plural = "Received vehicles"






class RegisteredVehicle(models.Model):
    # Foreign key to ReceivedVehicle model
    # received_vehicle = models.ForeignKey(receivedvehicle, on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ('N', 'The vehicle has not been issued to the owner.'),
        ('y', 'The vehicle has been issued to the owner.'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='RN')

    sku = models.CharField(max_length=500, blank=True)
    vehicle_id=models.CharField(max_length=500, blank=True)
    Plate_number=models.CharField(max_length=500, blank=True)
    vin_code = models.CharField(max_length=500, blank=True)
    manufacture = models.CharField(max_length=1000, null=True, blank=True)
    country = models.CharField(max_length=1000, null=True, blank=True)
    series = models.CharField(max_length=1000, null=True, blank=True)
    model_name = models.CharField(max_length=225, null=True, blank=True)
    factory_name = models.CharField(max_length=1000, null=True, blank=True)
    color = models.CharField(max_length=500, null=True, blank=True)
    eu_type_approval = models.CharField(max_length=500, null=True, blank=True)
    body_type = models.CharField(max_length=500, null=True, blank=True)
    steering_power = models.CharField(max_length=500, null=True, blank=True)
    wheels = models.CharField(max_length=500, null=True, blank=True)
    screen = models.CharField(max_length=500, null=True, blank=True)
    lights = models.CharField(max_length=500, null=True, blank=True)
    cargo_compartments = models.CharField(max_length=500, null=True, blank=True)
    communication_terminal = models.CharField(max_length=500, null=True, blank=True)
    date_of_manufacture = models.DateField(null=True, blank=True)
    orderer = models.CharField(max_length=1000, null=True, blank=True)
    orderer_phone = models.CharField(max_length=500, null=True, blank=True)
    orderer_email = models.EmailField(null=True, blank=True)
    # importer = models.CharField(max_length=100, null=True, blank=True)
    # dealer = models.CharField(max_length=100, null=True, blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    # public_id = models.IntegerField(null=True)

    # Other fields for RegisteredVehicle model if needed
    # ...

    def __str__(self):
        return f"{self.sku} - {self.status}"