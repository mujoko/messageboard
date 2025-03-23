from django.shortcuts import render

from posts.models import Post
from django.views.generic import ListView  # new



# Create your views here.
class PostList(ListView):  # new
    model = Post
    template_name = "post_list.html"