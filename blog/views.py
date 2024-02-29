from django.shortcuts import render
from django.core.cache import cache
from .models import Post

def blog_list(request):
    # Check if blog posts are cached
    posts = cache.get('blog_posts')

    if not posts:
        # Fetch blog posts from database
        posts = Post.objects.all()
        # Cache blog posts for 5 minutes
        cache.set('blog_posts', posts, 300)

    return render(request, 'blog.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})

def about(request):
    return render(request, 'about.html')