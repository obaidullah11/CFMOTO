from django.db import models

# Create your models here.
class VehicleGarage(models.Model):
    Manufacturer = models.CharField(max_length=100, blank=True, null=True)
    series = models.CharField(max_length=100, blank=True, null=True)
    Factory_name = models.CharField(max_length=100, blank=True, null=True)
    model_name = models.CharField(max_length=100, blank=True, null=True)
    eu_type = models.CharField(max_length=100, blank=True, null=True)
    steering_power = models.CharField(max_length=100, blank=True, null=True)
    wheels = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    lights = models.CharField(max_length=100, blank=True, null=True)
    screen = models.CharField(max_length=100, blank=True, null=True)
    cargo_compartment = models.CharField(max_length=100, blank=True, null=True)
    communication_terminal = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    sku = models.CharField(max_length=100, blank=True, null=True)
    user_email = models.EmailField(blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    user_phone = models.CharField(max_length=15, blank=True, null=True)
    approved_by_admin = models.BooleanField(default=False, verbose_name='Approved by Admin')
    
    def __str__(self):
        return f"{self.Factory_name} - {self.series} - {self.model_name}"