from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse , Http404
from django.urls import reverse
from .models import Post
import logging
# posts = [
#         {'title':'Post 1', 'content' : 'content of post 1', 'id':1},
#         {'title':'Post 2', 'content' : 'content of post 2', 'id':2},
#         {'title':'Post 3', 'content' : 'content of post 3', 'id':3},
#         {'title':'Post 4', 'content' : 'content of post 4', 'id':4},
#         {'title':'Post 5', 'content' : 'content of post 5', 'id':5},
#         {'title':'Post 6', 'content' : 'content of post 6', 'id':6}
#     ]

def index(request):
    page_title = "Robert Posts"
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'page_title': page_title, 'posts' : posts})

def detail(request, slug):

    post = get_object_or_404(Post,slug=slug)
    # logger = logging.getLogger("Testing..")
    # logger.debug(f'post is {post}')
    return render(request, 'blog/details.html',{'post':post})

