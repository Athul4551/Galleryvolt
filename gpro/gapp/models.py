from django.db import models
class Gallery(models.Model):
    feedimage=models.ImageField(upload_to='gallery_images/')
# Create your models here.
