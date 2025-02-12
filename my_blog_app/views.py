from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView
from django.views import View
from django.urls import reverse
from .models import Post
from .form import CommentForm
# Create your views here.


class StartingPageView(ListView):
    template_name = "my_blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    paginate_by = 3


class AllPostsView(ListView):
    template_name = "my_blog/all_posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"


class PostDetailView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        context = {
                   "post": post, 
                   "tags":post.tags.all(), 
                   "comment_form": CommentForm(), 
                   "comments": post.comments.all().order_by("-date")
                   }
        return render(request, "my_blog/post_detail.html", context)
    
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))
        context = {
            "post": post, 
            "comment_form": comment_form, 
            "comments": post.comments.all().order_by("-date")
            }
        return render(request, "my_blog/post_detail.html", context)
    
class ReadLaterView(View):
    def get(self, request):
        stored_posts_slugs = request.session.get("stored_posts")
        stored_posts = Post.objects.filter(slug__in=stored_posts_slugs)
        context = {"stored_posts": stored_posts}
        return render(request, "my_blog/stored_posts.html", context)
    

    def post(self, request):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is None:
            stored_posts = []
        post_slug = request.POST["post_slug"]
        if post_slug not in stored_posts:
            stored_posts.append(post_slug)
        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")