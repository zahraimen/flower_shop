from django.shortcuts import render
from django.views import generic
# Create your views here.
from .models import Flower
from .forms import FlowerCreation


class FlowerListView(generic.ListView):
    model = Flower
    template_name = 'flowers/flower_list.html'
    context_object_name = 'flowers'


class FlowerDetailView(generic.DetailView):
    model = Flower
    template_name = 'flowers/flower_detail.html'


class FlowerCreateView(generic.CreateView):
    form_class = FlowerCreation
    template_name = 'flowers/flower_create.html'