from django.db import models
from django.utils import timezone
from vehicles.models import Vehicle
from Garage.models import VehicleGarage

# Create your models here.
class DeliveredVehicle(models.Model):
    vehicle_system_id = models.CharField(max_length=20, unique=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    
    STATUS_CHOICES = (
        ('OW', 'On the way - Not received yet'),
        ('AW', 'Arrived at warehouse'),
        ('TD', 'transfer to dealer'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        # Check if the instance is being created (not updated)
        if not self.vehicle_system_id:
            last_vehicle = DeliveredVehicle.objects.order_by('-vehicle_system_id').first()
            if last_vehicle:
                last_id = int(last_vehicle.vehicle_system_id.split('-')[-1])
            else:
                last_id = 0
            new_id = last_id + 1
            self.vehicle_system_id = f"{1000:04d}-{new_id:04d}"  # Format as "1000-xxxx"
        super(DeliveredVehicle, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.vehicle_system_id} "

class ConfirmVehicle(models.Model):
    STATUS_CHOICES = (
        ('approved', 'Approved Vehicle for Garage'),
        ('not_approved', 'Not Approved Vehicle for Garage'),
    )
    
    vehicle_garage = models.ForeignKey(VehicleGarage, on_delete=models.CASCADE)
    # confirmed_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Replace with your User model if different
    confirmation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_approved')
    
    def __str__(self):
        return f"Confirmed Vehicle: {self.vehicle_garage.Factory_name} - {self.vehicle_garage.series} - {self.vehicle_garage.model_name}"