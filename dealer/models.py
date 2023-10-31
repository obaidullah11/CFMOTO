# from django.db import models
# from users.models import User
# from vehicles.models import Vehicle,Factory
# from django.utils import timezone

# # # from django.utils import timezone
# # # from products.models import Product

# # # class History(models.Model):
# # #     timestamp = models.DateTimeField(default=timezone.now)
# # #     description = models.CharField(max_length=200)
# # #     product = models.ForeignKey(Product, on_delete=models.CASCADE)

# # #     def __str__(self):
# # #         # return f"{self.timestamp} - {self.description} - Product: {self.product.sku}"


# # # class Order(models.Model):
# # #     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
   
   
    
    
# # #     STATUS_CHOICES = (
# # #         ('PN', 'pending '),
# # #         ('RC', 'recieved '),

# # #         ('AR', 'Assaign registration number'),
# # #         ('DU', 'deliverd to user'),
        
# # #     )
# # #     status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='PN')

# # #     def __str__(self):
# # #         return f"Order ID: {self.pk} - {self.vehicle}"
    










# class newreceivedvehicle(models.Model):
#     manufacturing_date = models.DateTimeField(default=timezone.now)
#     vin_code = models.CharField(max_length=17,blank=True,null=True)
#     vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
   
#     STATUS_CHOICES = (
#         ('PN', 'pending'),
#         ('RC', 'received'),
#         ('AR', 'Assign registration number'),
#         ('DU', 'delivered to user'),
#     )
#     status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='PN')
#     name_received_product = models.CharField(max_length=100)
#     class Meta:
#         db_table = 'dealer_receivedvehicle'

#     def save(self, *args, **kwargs):
#         # If the status is 'RC', set the name_received_product field to 'Factory'
#         if self.status == 'RC':
#             self.name_received_product = 'Factory'
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.manufacturing_date} - {self.vehicle} - {self.get_status_display()}"
    