from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    catch_date = models.DateTimeField(auto_now=True)