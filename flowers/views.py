from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Flower
from .forms import FlowerCreation, UserCommentForm, AnonymousCommentForm


class FlowerListView(generic.ListView):
    queryset = Flower.objects.order_by('-id')
    model = Flower
    template_name = 'flowers/flower_list.html'
    context_object_name = 'flowers'
    paginate_by = 4


class FlowerDetailView(generic.DetailView):
    model = Flower
    template_name = 'flowers/flower_detail.html'
    context_object_name = 'flower'

    def get_form_class(self):
        user = self.request.user
        return UserCommentForm if user.is_authenticated else AnonymousCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.filter(is_active=True)
        context['form'] = self.get_form_class()()
        return context

    def post(self, **kwargs):
        request = self.request
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if isinstance(form, UserCommentForm):
                comment.user = request.user
            comment.flower = self.get_object()
            comment.save()
            return redirect(comment.get_absolute_url())
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)


class FlowerCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = FlowerCreation
    template_name = 'flowers/flower_create.html'


class FlowerUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Flower
    fields = ['title', 'seller', 'description', 'price', 'cover', ]
    template_name = 'flowers/flower_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.seller == self.request.user.username


class FlowerDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Flower
    template_name = 'flowers/flower_delete.html'
    success_url = reverse_lazy('flower_list')

    def test_func(self):
        obj = self.get_object()
        return obj.seller == self.request.user.username
