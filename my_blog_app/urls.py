from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartingPageView.as_view(), name='home'),  # Home page (latest posts)
    path('post/<int:id>/', views.PostDetailView.as_view(), name='post_detail'),  # Post detail page
    path('all_posts', views.AllPostsView.as_view(), name='all_posts'),  # All Posts page
]
