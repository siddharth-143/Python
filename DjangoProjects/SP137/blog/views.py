from django.db import models
from django.http.response import Http404
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['id']
    paginate_by = 3
    paginate_orphans = 1

    def get_context_data(self, **kwargs):
        try:
            return super(PostListView, self).get_context_data(**kwargs)
        except Http404:
            self.kwargs['page'] = 1
            return super(PostListView, self).get_context_data(**kwargs)

    # def paginate_queryset(self, queryset, page_size):
    #     try:
    #         return super(PostListView, self).paginate_queryset(queryset, page_size)
    #     except Http404:
    #         self.kwargs['page'] = 1
    #         return super(PostListView, self).paginate_queryset(queryset, page_size)
