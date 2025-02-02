from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    ROLE_OPTION=[
        ('Admin','Admin'),
        ('User','User'),

    ]
    user_name=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=255)
    role=models.CharField(max_length=9,choices=ROLE_OPTION)
    email=models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.user_name
    
class Customer(models.Model):
    GENDER_CHOICES=[
        ('M','MALE'),
        ('F','FEMALE'),
    ]
    
    customer_name=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=13,null=True,blank=True,unique=True)
    address=models.CharField(max_length=60)
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES)
    email=models.EmailField(unique=True)

    def __str__(self):
        return f"{self.customer_name}"
    
class Categories(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"
    


class Product(models.Model):
    pro_name=models.CharField(max_length=20)
    price=models.IntegerField()
    #image=models.
    category=models.ForeignKey('Categories', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.pro_name}"
    

class Order(models.Model):
    order_date=models.DateField()
    # product=models.ForeignKey('Product',on_delete=models.CASCADE,default=1)
    total_price=models.IntegerField()
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    def _str_(self):
        return f"{self.customer_name}"
    




class Suppliers(models.Model):
    supp_name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    email=models.EmailField(max_length=200)
    phone_number=models.CharField(max_length=13,blank=True,null=True) 
    def __str__(self):
        return f"{self.supp_name}"        


class Payment(models.Model):
     payment_data=models.DateField()
     amount=models.IntegerField()
     payment_method=models.IntegerField()
     order=models.OneToOneField(Order, on_delete=models.CASCADE)

     def __str__(self):
         return f"{self.amount}"