from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Flower(models.Model):
    title = models.CharField(max_length=225)
    seller = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('flower_detail', args=[self.id])
