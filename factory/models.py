from django.db import models
from users.models import User
from vehicles.models import Vehicle





# class Factory_details(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.name
# Create your models here.
class newOrder(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    dealer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='new_dealer_orders')
    
    
    # factory = models.ForeignKey(Factory_details, on_delete=models.CASCADE)
   
    STATUS_CHOICES = (
        ('W', 'Waiting for Receive'),
        ('P', 'In Process'),
        ('S', 'Shipped out of the Factory'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='W')

    def __str__(self):
        return f"Order ID: {self.pk} - {self.vehicle}"