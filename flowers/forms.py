from django import forms
from .models import Flower, Comment


class FlowerCreation(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ('title', 'seller', 'description', 'price', 'cover')


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'recommend',)


class AnonymousCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('fullname', 'email', 'text', 'recommend',)
