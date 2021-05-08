from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog

# Create your views here.

def home(request):
    songBlog = Blog.objects.all()
    return render(request,'home.html',{'songBlog' : songBlog})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html' ,{'blog' : blog_detail})

def new(request):
    return render(request,'new.html')

def create(request):
    freshBlog = Blog()
    freshBlog.blog_title = request.POST['songTitle']
    freshBlog.blog_writer = request.POST['songWriter']
    freshBlog.blog_body = request.POST['songBody']
    freshBlog.blog_date = timezone.now()
    freshBlog.save()
    return redirect('detail',freshBlog.id)


def edit(request, blog_id):
    reviseBlog = Blog.objects.get(id = blog_id)
    return render(request, 'edit.html', {'blog' : reviseBlog})


def update(request, blog_id):
    updateBlog = Blog.objects.get(id = blog_id)
    updateBlog.blog_title = request.POST['songTitle']
    updateBlog.blog_writer = request.POST['songWriter']
    updateBlog.blog_body = request.POST['songBody']
    updateBlog.blog_date = timezone.now()
    updateBlog.save()
    return redirect('detail',updateBlog.id)


def delete(request, blog_id):
    deleteBlog =  Blog.objects.get(id = blog_id)
    deleteBlog.delete()
    return redirect('home')