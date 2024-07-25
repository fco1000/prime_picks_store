from django.db import models 
from .products import Product
from .customer import Customer 
import datetime 
   
class Size(models.Model):
    size = models.IntegerField()
    
    def __str__(self):
        return str(self.size)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    quantity = models.IntegerField(default=1) 
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.IntegerField() 
    address = models.CharField(max_length=50, default='', blank=True) 
    phone = models.CharField(max_length=50, default='', blank=True) 
    date = models.DateField(default=datetime.datetime.today) 
    status = models.BooleanField(default=False)
    
    def placeOrder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date') 
 