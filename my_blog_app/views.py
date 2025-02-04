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
        return render(request, "my_blog/post_detail.html", {"post": post, "tags":post.tags.all(), "comment_form": CommentForm()})
    
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse("post_detail", args=[slug]))
        return render(request, "my_blog/post_detail.html", {"post": post, "comment_form": comment_form})