from django.db import models
from django.contrib.auth.models import User
class Gallery(models.Model):
    feedimage=models.ImageField(upload_to='gallery_images/')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
# Create your models here.
