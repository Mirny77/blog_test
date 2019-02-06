from django.shortcuts import render

from .models import *

from django.views.generic.list import ListView


class ListBlog(ListView):
    """Список
            """
    model = Post
    queryset = Post.objects.filter(sub=True).order_by('-created')

    context_object_name = "posts"
    template_name = "blog.html"

