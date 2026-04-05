from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse , Http404
from django.urls import reverse
from .models import Post, AboutUs
from django.core.paginator import Paginator
import logging
from .forms import Contactform
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
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/index.html', {'page_title': page_title, 'page_obj' : page_obj})

def detail(request, slug):

    post = get_object_or_404(Post,slug=slug)
    related_posts = Post.objects.filter(category = post.category).exclude(pk=post.id)
    # logger = logging.getLogger("Testing..")
    # logger.debug(f'post is {post}')
    return render(request, 'blog/details.html',{'post':post,'related_posts':related_posts})

def contact(request):
    if request.method == "POST":
        form = Contactform(request.POST)
        logger = logging.getLogger("Testing")
        if form.is_valid():
            logger.debug(f'Post Data is {form.cleaned_data['name']}')
            success_message = 'You email Has be sent'
            return render(request,'blog/contact.html',{'form':form, 'success_message':success_message})
        else:
            logger.debug(f'Form Validation error')  
        return render(request,'blog/contact.html',{'form':form, })
    return render(request,'blog/contact.html')

def about_us(request):
    about_content = AboutUs.objects.first().content
    return render(request,'blog/about.html',{'about_content':about_content})