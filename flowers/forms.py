from django import forms
from .models import Flower


class FlowerCreation(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ('title', 'seller', 'description', 'price',)



