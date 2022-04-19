from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Customer, Comment
from django.contrib.auth.models import User
from .forms import PostForm, UserForm, CustomerForm, CommentForm
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
import datetime

class Home(generic.View):
    def get(self, request):
        date_posted = datetime.datetime.now().year
        context = {
            'date_posted':date_posted,
        }
        return render(request, "my_app/home.html", context)

def forum(request):
    date_posted = datetime.datetime.now().year
    model = Post.objects.all().order_by("id")
    p = Paginator(Post.objects.all(), 2)
    page = request.GET.get("page")
    venues = p.get_page(page)
    if request.method == "POST":
        cautat = request.POST.get("cautat")
        lookup = (Q(title__icontains = cautat))
        new_model = Post.objects.filter(lookup)
        return render(request, "my_app/forum.html", {'model':model, 'date_posted':date_posted, 'new_model':new_model, 'cautat':cautat, 'venues':venues})
    else:
        return render(request, "my_app/forum.html", {'model':model, 'date_posted':date_posted, 'venues':venues})

def search_forum(request):
    if request.method == "POST":
        date_posted = datetime.datetime.now().year
        cautat = request.POST.get("cautat")
        lookup = (Q(title__icontains = cautat))
        model_cautat = Post.objects.filter(lookup)
        context = {
            'date_posted':date_posted,
            'model_cautat':model_cautat,
            'cautat':cautat,
        }
        return render(request, "my_app/search_forum.html", context)

def forum_details(request, pk):
    date_posted = datetime.datetime.now().year
    model = Post.objects.get(id=pk)
    new_model = Post.objects.filter(id=pk)
    comment_model = Comment.objects.all()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect("forum")
    context = {
        'model':model,
        'date_posted':date_posted,
        'new_model':new_model,
        'form':form,
        'comment_model':comment_model,
    }
    return render(request, "my_app/forum_details.html", context)

def members(request):
    date_posted = datetime.datetime.now().year
    context = {
        'date_posted':date_posted,
    }
    return render(request, "my_app/members.html", context)

def register_user(request):
    date_posted = datetime.datetime.now().year
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:sign_up')
        else:
            raise Http404
    context = {
        'date_posted':date_posted,
        'form':form,
    }
    return render(request, 'my_app/register.html', context)

def sign_up(request):
    date_posted = datetime.datetime.now().year
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user  = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid")
    context = {
        'date_posted':date_posted,
    }
    return render(request, "my_app/signup.html", context)

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def account(request, pk):
    date_posted = datetime.datetime.now().year
    model = User.objects.get(id=pk)
    anunt = model.post_set.all()
    context = {
        'model':model,
        'date_posted':date_posted,
        'anunt':anunt,
    }
    return render(request, "my_app/account.html", context)

@login_required
def add_post(request, pk):
    date_posted = datetime.datetime.now().year
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            raise Http404
    context = {
        'date_posted':date_posted,
        'form':form,
    }
    return render(request, "my_app/add_post.html", context)

##################CRUD####################

@login_required
def update_post(request, pk):
    date_posted = datetime.datetime.now().year
    model = Post.objects.get(id=pk)
    form = PostForm(instance=model)
    if request.method == "POST":
        form = PostForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
        else:
            raise Http404
    context = {
        'model':model,
        'form':form,
        'date_posted':date_posted,
    }
    return render(request, "my_app/update_post.html", context)

@login_required
def delete_post(request, pk):
    date_posted = datetime.datetime.now().year
    model = Post.objects.get(id=pk)
    if request.method == "POST":
        model.delete()
        return redirect("home")
    context = {
        'model':model,
        'date_posted':date_posted,
    }
    return render(request, "my_app/delete_post.html", context)

# Create your views here.
