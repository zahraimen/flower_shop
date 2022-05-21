from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
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


class FlowerUpdateView(generic.UpdateView):
    model = Flower
    fields = ['title', 'seller', 'price']
    template_name = 'flowers/flower_update.html'


class FlowerDeleteView(generic.DeleteView):
    model = Flower
    template_name = 'flowers/flower_delete.html'
    success_url = reverse_lazy('flower_list')
