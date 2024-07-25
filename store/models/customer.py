from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=100)
    
    def register(self):
        self.save()
        
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        
    def is_exists(self):
        if Customer.objects.filter(email=self.email):
            return True
        
        return False

class County(models.Model):
    county = models.CharField(max_length=250)
    
    def __str__(self):
        return str(self.county)
    
class SubCounty(models.Model):
    sub_county = models.CharField(max_length=250)
    
    def __str__(self):
        return str(self.sub_county)

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    phone = models.CharField(max_length=250)
    county = models.ForeignKey(County, on_delete=models.SET_NULL,null = True)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.SET_NULL,null=True)