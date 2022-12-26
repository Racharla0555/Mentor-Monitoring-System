from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class mentors(models.Model):
    name=models.CharField(max_length=49)
    branch=models.CharField(max_length=98)
    batch=models.CharField(max_length=29)
    hall_ticket=models.CharField(max_length=10)
    sem1=models.CharField(max_length=10)
    sem2=models.CharField(max_length=30)
    remarks=models.CharField(max_length=100)
    attendance=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

