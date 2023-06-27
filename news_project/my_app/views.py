from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from datetime import datetime
from .forms import LoginForm, SignUpForm, CustomUpdateUser, PostCreationForm
from IPython import embed
from .models import CustomUser, Post
from django.views.generic.edit import CreateView
from django.conf import settings
import os


TIME = datetime.now()
# Create your views here.


def serve_home(request):
    return render(request=request, template_name='my_app/base.html', context={'date': TIME})

def site_logout(request):
    logout(request)
    return redirect("home")

def site_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, template_name="my_app/form.html", context={'form': form})

def serve_signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = "basic_user"
            user.save()
            login(request, user)
            return redirect('home')


    return render(request=request, template_name="my_app/form.html", context={"form":form})

def test(request):
    return render(request=request, template_name='my_app/test1.html', context={'date': datetime.now()})

def serve_update_account(request):
    user = request.user
    form = CustomUpdateUser(instance=user, include_user_type=False)
    del form.fields['password']
    if request.method == 'POST':
        form = CustomUpdateUser(request.POST, instance=request.user, include_user_type=False)
        del form.fields['password']
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request=request, template_name='my_app/form.html', context={'form':form})

def serve_staff_edit_accounts(request, user_id):
    user = CustomUser.objects.get(id = user_id)
    form = CustomUpdateUser(instance=user, include_user_type=True)
    if request.method == 'POST':
        form = CustomUpdateUser(request.POST, instance=user , include_user_type=True)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request=request, template_name='my_app/form.html', context={'form':form})

def test_display_users(request):
    users = CustomUser.objects.all()
    return render(request=request, template_name='my_app/displayusers.html', context={"customusers":users})

def add_post(request):
    form = PostCreationForm()
    form.initial['writer'] = request.user
    form.fields['writer'].disabled = True

    if request.method == 'POST':
        form = PostCreationForm(request.POST, request.FILES)
        form.initial['writer'] = request.user
        form.fields['writer'].disabled = True
        if form.is_valid():
            post = form.save()
            if form.cleaned_data['images']:
                img = form.cleaned_data['images']
                path = os.path.join(settings.BASE_DIR, 'my_app','static', 'post_images', f'postid={post.id}title.jpg')
                with open (path, 'wb') as fh:
                    for chunk in img.chunks():
                        fh.write(chunk) 
            return redirect('home')
    return render(request=request, template_name='my_app/form.html', context={'form':form})

def serve_sport(request):
    articles = Post.objects.filter(category='sport')
    return render(request=request, template_name='my_app/sport.html', context={"articles":articles})

def serve_health(request):
    articles = Post.objects.filter(category='health')
    return render(request=request, template_name='my_app/health.html', context={"articles":articles})

def serve_article(request, article_id):
    article = Post.objects.get(id=article_id)
    return render(request=request, template_name="my_app/article.html", context={"article":article})