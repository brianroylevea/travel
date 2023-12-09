from django.db import models

class destination(models.Model):
    name  = models.CharField(max_length=100)
    desc =models.TextField()
    Price = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    offer : models.BooleanField()

# Create your models here.
