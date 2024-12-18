from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "my_blog/index.html",{
        "posts": latest_posts
    })

def all_posts(request):
    all_posts = Post.objects.all()
    return render(request, "my_blog/all_posts.html", {
        "posts": all_posts
    })

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  # Retrieve the post or return 404 if not found
    return render(request, "my_blog/post_detail.html", {
        "post": post
    })