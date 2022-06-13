from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


# Create your models here.
class Flower(models.Model):
    title = models.CharField(max_length=225)
    seller = models.CharField(max_length=225)
    description = models.TextField()
    price = models.IntegerField()
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('flower_detail', args=[self.id])


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
