from django.shortcuts import render
from .models import Post

def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})

def about(request):
    return render(request, 'about.html')