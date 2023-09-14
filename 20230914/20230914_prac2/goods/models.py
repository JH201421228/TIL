from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=99, decimal_places=2)
    is_published = models.BooleanField(default=True)
    is_it_okay = models.BooleanField(default=False)
    date1 = models.DateField(auto_now_add=True)
    date2 = models.DateTimeField(auto_now=True)
