from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post
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
    context_object_name = "posts"


class PostDetailView(DetailView):
    template_name = "my_blog/post_detail.html"
    model = Post
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tags.all()
        return context