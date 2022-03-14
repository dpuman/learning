from django.http import Http404
from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
# Create your views here.


class BlogView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    ordering = ['id']
    paginate_by = 3
    paginate_orphans = 1

    def get_context_data(self, *args, **kwargs):
        try:
            return super(BlogView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(BlogView, self).get_context_data(*args, **kwargs)


class BlogDetails(DetailView):
    model = Blog
    template_name = 'blog/blog-details.html'
