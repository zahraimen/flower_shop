from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    city = models.CharField(max_length=200)


class Seller(models.Model):
    seller = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.PositiveIntegerField(max_length=11)
