from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse , Http404
from django.urls import reverse
from .models import Post, AboutUs 
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import logging
from .forms import Contactform , Registerform , Loginform , Forgotpassword ,Resetpassword
from django.contrib import messages
from django.contrib.auth import authenticate , login as auth_login , logout as auth_logout
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
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
    about_content = AboutUs.objects.first()
    if about_content is None or not about_content.content:
        about_content = "Default Content is here"
    else:
        about_content = about_content.content
    return render(request,'blog/about.html',{'about_content':about_content})

def register(request):
    form =Registerform()
    if request.method == "POST":
        form = Registerform(request.POST)
        if form.is_valid():
            user =form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'User Has been created')
            return redirect('blog:login')
        
    return render(request,'blog/register.html',{'form':form})

def login(request):
    form = Loginform()
    
    if request.method == "POST":
        form = Loginform(request.POST)
        if form.is_valid():
            user = form.user_cache
            if user is not None:
                auth_login(request,user)
                print("Login Success")
                return redirect('blog:dashboard')
                
        
    return render(request,'blog/login.html',{'form':form})


def dashboard(request):
    return render(request,'blog/dashboard.html')

def logout(request):
    auth_logout(request)
    return redirect('blog:index')

def forgot_password(request):
    form = Forgotpassword()
    if request.method == "POST":
        form = Forgotpassword(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = form.user_cache
            # User password reset
            token = default_token_generator.make_token(user)
            uid =urlsafe_base64_encode(force_bytes(user.pk))
            current_site = get_current_site(request)
            domain = current_site.domain
            subject = "Password Reset request "
            message = render_to_string('blog/reset_email_password.html',{
                'domain':domain,
                'uid':uid,
                'token':token
            })
            
            send_mail(subject,message,'noreply@lucifer.com',[email])
            messages.success(request,"The email has been sent successfully")
    return render(request,'blog/forgot_password.html',{'form':form})

def reset_password(request,uidb64, token):
    form=Resetpassword()
    if request.method=="POST":
        form = Resetpassword(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get("new_password")
            try:
                uid =urlsafe_base64_decode(uidb64)
                user = User.objects.get(pk=uid)
            except(TypeError,ValueError,OverflowError,User.DoesNotExist):
                user = None
            
            if user is not None and default_token_generator.check_token(user,token):
                user.set_password(new_password)
                user.save()
                messages.success(request,'Your Password has been updated')
                return redirect('blog:login')
            else:
                messages.error(request,"The password reset form is invalid")
    return render(request,'blog/reset_password.html',{'form':form})