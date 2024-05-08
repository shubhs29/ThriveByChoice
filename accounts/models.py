from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    sustainability_rating = models.DecimalField(max_digits=3, decimal_places=2)
    environmental_impact = models.TextField()
    ethical_sourcing = models.TextField()
    certifications = models.TextField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_products = models.ManyToManyField(Product, blank=True)

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)