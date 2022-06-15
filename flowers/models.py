from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


# Create your models here.
class Flower(models.Model):
    title = models.CharField(max_length=225)
    seller = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    description = models.TextField()
    price = models.IntegerField()
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('flower_detail', args=[self.id])


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE, related_name='comments')
    fullname = models.CharField(max_length=128, null=True)
    email = models.EmailField(null=True)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    recommend = models.BooleanField(default=True)

    def __str__(self):
        return self.text

    def get_author_name(self):
        try:
            return self.user.username
        except AttributeError:
            return self.fullname

    def get_absolute_url(self):
        return reverse('flower_detail', args=[self.flower.id]) + f'#{self.id}'
