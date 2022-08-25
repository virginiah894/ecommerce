from re import M
from django.db import models

# Create your models here.
class  Category(models.Model):
    category_name = models.CharField(max_length=40)
    def __str__(self):
        return self.category_name

class  Product(models.Model):
    product_name= models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    image = models.ImageField()

    quantiy = models.IntegerField()
    price= models.IntegerField()
    category_name = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class  Order(models.Model):
    product_name= models.ForeignKey(Product,on_delete=models.CASCADE)
    delivery_location = models.CharField(max_length=69)
    def __str__(self):
        return self.product_name
    

