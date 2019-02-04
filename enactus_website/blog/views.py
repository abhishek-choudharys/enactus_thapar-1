from django.views.generic import ListView, DetailView,TemplateView
from . models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    template_name = 'discussion.html'

class BlogDetailView(DetailView):

    model = Post

    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post

    template_name = 'post_new.html'

    fields = '__all__'

class BlogUpdateView(UpdateView):

    model = Post

    fields = ['title', 'body']

    template_name = 'post_edit.html'

class BlogDeleteView(DeleteView):

    model = Post

    template_name = 'post_delete.html'

    success_url = reverse_lazy('discussion')