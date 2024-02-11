from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Res(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL,null = True , blank=True )
    res_name=models.CharField(max_length=100)
    res_description=models.TextField()
    res_image=models.ImageField(upload_to="res")
