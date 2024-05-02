from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=150)
    ism = models.CharField(max_length=50)
    familiya = models.CharField(max_length=53)
    email = models.EmailField
    parol = models.CharField(max_length=16)
    image = models.ImageField(upload_to='user/images/')

