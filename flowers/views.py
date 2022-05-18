from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import Flower


class FlowerListView(generic.ListView):
    model = Flower
    template_name = 'flowers/flower_list.html'
    context_object_name = 'flowers'
