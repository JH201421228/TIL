from django.db import models

# Create your models here.
class App(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank=True)
    