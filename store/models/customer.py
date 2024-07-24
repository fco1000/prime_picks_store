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