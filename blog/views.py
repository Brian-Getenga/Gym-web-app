from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Bookmark, Like, Category, Tag
#from .forms import BlogPostForm  # Import if you have a form for creating/editing posts

def blog_list(request, category_id=None):
    categories = Category.objects.all()
    search_query = request.GET.get('search', '')
    
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        posts = BlogPost.objects.filter(category=category, title__icontains=search_query)
    else:
        posts = BlogPost.objects.filter(title__icontains=search_query)
    
    return render(request, 'blog/blog_list.html', {'posts': posts, 'categories': categories, 'search_query': search_query})

def blog_post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        if 'bookmark' in request.POST:
            if request.user.is_authenticated:
                bookmark, created = Bookmark.objects.get_or_create(user=request.user, post=post)
                if not created:
                    bookmark.delete()
                return redirect('blog:blog_post_detail', id=post.id)
        elif 'like' in request.POST:
            if request.user.is_authenticated:
                like, created = Like.objects.get_or_create(user=request.user, post=post)
                if not created:
                    like.delete()
                return redirect('blog:blog_post_detail', id=post.id)
    return render(request, 'blog/blog_post_detail.html', {'post': post})

@login_required
def bookmark_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, post=post)
    if not created:
        bookmark.delete()
    return redirect('blog:blog_post_detail', id=post.id)

@login_required
def like_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect('blog:blog_post_detail', id=post.id)
