from django.urls import path
from . import views

urlpatterns = [
    path('', views.StartingPageView.as_view(), name='home'),  # Home page (latest posts)
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),  # Post detail page
    path('all_posts', views.AllPostsView.as_view(), name='all_posts'),  # All Posts page
    path('read-later', views.ReadLaterView.as_view(), name='read-later'),  # Read later page
]
