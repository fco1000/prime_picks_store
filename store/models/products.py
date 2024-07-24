from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    desciption = models.CharField(max_length=2500,default='',blank=True,null=True)
    image = models.ImageField(upload_to='uploads/products/')
    
    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_products_by_category(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
        
    