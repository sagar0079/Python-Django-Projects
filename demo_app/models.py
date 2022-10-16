# type: ignore
from urllib import request
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class FoodList(models.Model):
    user_name = models.ForeignKey(User,on_delete = models.CASCADE,default = 1)
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=100)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://www.kindpng.com/picc/m/79-798754_hoteles-y-centros-vacacionales-dish-placeholder-hd-png.png")

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('demo_app:food_detail',kwargs={'pk':self.pk})

    
    



