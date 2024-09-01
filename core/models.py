from django.db import models

# Create your models here.
class userdata(models.Model):
    Username=models.CharField(max_length=100,unique='True',null='True',blank='False',verbose_name='Username')
    Password=models.CharField(max_length=100,verbose_name='Password')
    def __str__(self):
        return self.Username

class Customers(models.Model):
    name = models.CharField(max_length= 100, null='True',blank='False', verbose_name='name')
    address = models.CharField(max_length= 100,null='True', blank='False', verbose_name='address')
    phone = models.CharField(max_length= 100, null = 'True', blank='False', verbose_name='phone')
    email = models.CharField(max_length= 100, null = 'True', blank='False', verbose_name='email')
    picture=models.ImageField(upload_to='images/',null='True',blank='False', verbose_name='image')
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length= 100, null='True',blank='False', verbose_name='name')
    price = models.CharField(max_length= 100,null='True', blank='False', verbose_name='price')
    picture=models.ImageField(upload_to='images/',null='True',blank='False', verbose_name='productimage')
    def __str__(self):
        return self.name
    

