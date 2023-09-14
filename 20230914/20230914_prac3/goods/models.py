from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=99, decimal_places=2)
    is_published = models.BooleanField(default=True)
    haha = models.BooleanField(default=True)
    create_date = models.DateField(auto_now_add=True)
    now_date = models.DateTimeField(auto_now=True)
