from django.db import models
from django.conf import settings


# Create your models here.
class Pokemon(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_pokemons')
    name = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)