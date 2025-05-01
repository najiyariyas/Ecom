from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='Category')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='product_images/')  
    upload_date = models.DateField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Orders(models.Model):
    name=models.CharField(max_length=30)
    order_date=models.DateTimeField(auto_now_add=True)
    dispatch_date=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    def __str__(self):
        return self.name
class BestSellers(models.Model):  
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sold_count = models.IntegerField()
    pro=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class NewRelease(models.Model):
    product_name = models.CharField(max_length=255)
    release_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    pro=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
class Review(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name} on {self.product.name}"

