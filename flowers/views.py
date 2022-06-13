from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
# Create your views here.
from .models import Flower
from .forms import FlowerCreation, CommentForm


class FlowerListView(generic.ListView):
    model = Flower
    template_name = 'flowers/flower_list.html'
    context_object_name = 'flowers'
    paginate_by = 4


def book_detail_view(request, pk):
    # get flower object
    flower = get_object_or_404(Flower, pk=pk)
    # get flower comments
    flower_comments = flower.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.flower = flower
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()

    else:
        comment_form = CommentForm()

    return render(request, 'flowers/flower_detail.html',
                  {'flower': flower, 'comments': flower_comments, 'comment_form': comment_form})


# class FlowerDetailView(generic.DetailView):
#     model = Flower
#     template_name = 'flowers/flower_detail.html'


class FlowerCreateView(generic.CreateView):
    form_class = FlowerCreation
    template_name = 'flowers/flower_create.html'


class FlowerUpdateView(generic.UpdateView):
    model = Flower
    fields = ['title', 'seller', 'description', 'price', 'cover', ]
    template_name = 'flowers/flower_update.html'


class FlowerDeleteView(generic.DeleteView):
    model = Flower
    template_name = 'flowers/flower_delete.html'
    success_url = reverse_lazy('flower_list')
