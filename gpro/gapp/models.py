from django.db import models
class Gallery(models.Model):
    feedimage=models.ImageField(upload_to='image/')
# Create your models here.
