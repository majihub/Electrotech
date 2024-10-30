from django.db import models

# Create your models here.
class customers(models.Model):
    UserName=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Mobile=models.BigIntegerField()
    Password=models.CharField(max_length=100)
    Country=models.CharField(max_length=100,default='default')
    District=models.CharField(max_length=100,default='default')
    Address=models.TextField(default='default')
    def __str__(self):
        return self.UserName
class Products(models.Model):
    ProductName=models.CharField(max_length=100)
    ProductType=models.CharField(max_length=100)
    Description=models.TextField()
    Price=models.IntegerField()
    Image=models.ImageField(upload_to='static/images/products/')
    availability=models.IntegerField()
    def __str__(self):
        return self.ProductName
class Cart(models.Model):
    ProductID=models.ForeignKey(Products,on_delete=models.CASCADE)
    UserID=models.ForeignKey(customers,on_delete=models.CASCADE)
    Price=models.IntegerField()
    Quantity=models.IntegerField(default=1)
class Payment(models.Model):
    CardNumber=models.CharField(max_length=200)
    cvv=models.IntegerField()
    expiry=models.CharField(max_length=20)
    PaidUser=models.CharField(max_length=200)
class favourites(models.Model):
    UserID=models.ForeignKey(customers,on_delete=models.CASCADE)
    ProductID=models.ForeignKey(Products,on_delete=models.CASCADE)