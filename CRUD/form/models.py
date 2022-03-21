from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Base_User(User):
    phone = models.IntegerField(null=True)



class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_quantity = models.IntegerField()
    product_price = models.DecimalField(max_digits=5,decimal_places=3)
    product_desc = models.TextField(max_length=200) 

