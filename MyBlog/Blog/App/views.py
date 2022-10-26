from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse

from App.models import Post, AdminArticle

class AdminArticleListView(ListView):
    model = AdminArticle
    template_name = 'App/home.html'
    paginate_by = 3

class AdminArticleDetailView(DetailView):
    model = AdminArticle
    template_name = 'App/detail.html'

class PostView(CreateView):
    model = Post
    fields = ['title', 'author', 'text']
    template_name = 'App/post.html'

    def get_success_url(self):
        return reverse('blog:home')







