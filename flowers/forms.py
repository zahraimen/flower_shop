from django import forms
from .models import Flower, Comment


class FlowerCreation(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ('title', 'seller', 'description', 'price', 'cover')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'recommend',)
