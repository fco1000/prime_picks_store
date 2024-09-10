from django.db import models
from apps.cart.models import Order
 
class Delivery(models.Model):
    order = models.OneToOneField(Order, related_name='delivery', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    tracking_number = models.CharField(max_length=255, blank=True, null=True)
    shipped_at = models.DateTimeField(blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Delivery for Order {self.order.id} - {self.status}"
