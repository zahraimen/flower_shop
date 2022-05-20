from django.db import models


# Create your models here.
class Flower(models.Model):
    title = models.CharField(max_length=225)
    seller = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title
