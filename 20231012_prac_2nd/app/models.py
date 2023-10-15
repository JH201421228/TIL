from django.db import models

# Create your models here.
class App(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank=True)
    
class Comment(models.Model):
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)