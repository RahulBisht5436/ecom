from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.FloatField()
    discount=models.FloatField()
    category=models.CharField(max_length=100)
    image=models.CharField(max_length=500)

class order(models.Model):
    item=models.CharField(max_length=100)
    name=models.CharField(max_length=100,default='rahul')
    email=models.CharField(max_length=100,default='123@gamil.com')
    address=models.CharField(max_length=1000,default='wedwd')
    city=models.CharField(max_length=100,default='dwdwdw')
    zipcode=models.CharField(max_length=20,default='dwydyus')
    state=models.CharField(max_length=100,default='cystydys')

