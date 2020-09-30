from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 150,verbose_name = "入力して下さい")
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to = 'thumbnails/')

