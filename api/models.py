from django.db import models

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=100)
    pricec=models.IntegerField()
    stock=models.IntegerField()
    created_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    