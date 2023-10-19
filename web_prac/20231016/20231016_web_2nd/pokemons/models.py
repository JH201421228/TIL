from django.db import models

# Create your models here.
class Pokemons(models.Model):
    name = models.CharField(max_length=100)
    describe = models.TextField()
    catch_date = models.DateTimeField(auto_now=True)