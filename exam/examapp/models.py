from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    amount1 = models.CharField(max_length=100)
  
class Trangection(models.Model):
    userid = models.ForeignKey(Register, on_delete=models.CASCADE)
    user_name= models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    amount = models.IntegerField()