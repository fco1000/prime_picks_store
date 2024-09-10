from django.db import models
from apps.account.models import Customer
from apps.vendor.models import Vendor

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Shoe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, related_name='shoes', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='shoes', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='shoes', on_delete=models.CASCADE)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class ShoeVariant(models.Model):
    shoe = models.ForeignKey(Shoe, related_name='variants', on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='shoe_variant_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.shoe.name} - {self.color} - Size {self.size}"

class Review(models.Model):
    customer = models.ForeignKey(Customer, related_name='reviews', on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoe, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.customer} for {self.shoe.name}"