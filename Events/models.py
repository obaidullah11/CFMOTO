from django.db import models
from django.utils import timezone
from vehicles.models import Vehicle
# Create your models here.
HISTORICAL_CHOICES = (
        ('The vehicle order has been forwarded to the factory.', 'The vehicle order has been forwarded to the factory.'),
        ('The vehicle is out of production.', 'The vehicle is out of production.'),
        ('The vehicle is ready for transport from the factory.', 'The vehicle is ready for transport from the factory.'),
        ('The vehicle arrived at the MOTOHOBI warehouse.', 'The vehicle arrived at the MOTOHOBI warehouse.'),
        ('The vehicle has been transferred to the dealer.', 'The vehicle has been transferred to the dealer.'),
        ('The vehicle is registered and issued with a reg number', 'The vehicle is registered and issued with a reg number'),
        ('The vehicle has been issued to the owner.', 'The vehicle has been issued to the owner.'),
        ('',''),

    )

class vehiclehystory(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=200)
    historical_note = models.CharField(max_length=150, choices=HISTORICAL_CHOICES)
    vehicle = models.ForeignKey(Vehicle,null=True ,blank=True,on_delete=models.CASCADE)
    owner_email = models.EmailField(blank=True, null=True,)  # Allow the field to be blank and nullable
    plate_number = models.CharField(max_length=20, blank=True, null=True)  # Allow the field to be blank and nullable
    vin_code = models.CharField(max_length=20, blank=True, null=True)
    def __str__(self):
        return f"{self.timestamp} - {self.description} - Product: {self.vehicle.sku}"
    class Meta:
        verbose_name_plural = "Vehicle History"