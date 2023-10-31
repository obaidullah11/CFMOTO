from django.db import models
from Garage.models import VehicleGarage  # Replace with the actual import path
from users.models import User

class ApproveAdminVehicle(models.Model):
    STATUS_CHOICES = (
        ('approved', 'Approved by Admin'),
        ('not_approved', 'Not Approved by Admin'),
    )
    
    vehicle_garage = models.ForeignKey(VehicleGarage, on_delete=models.CASCADE)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE)  # Assuming you have a User model
    approval_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_approved')
    
    vin_code = models.CharField(max_length=17, null=True)  # VIN code field
    mileage = models.PositiveIntegerField()     # Mileage field
    front_image = models.ImageField(upload_to='vehicle_images/', blank=True, null=True)  # Front image field
    back_image = models.ImageField(upload_to='vehicle_images/',blank=True, null=True)   # Back image field

    def __str__(self):
        return f"Approved Vehicle: {self.vehicle_garage.Factory_name} - {self.vehicle_garage.series} - {self.vehicle_garage.model_name}"