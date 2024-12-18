from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name='home'),  # Home page (latest posts)
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Post detail page
    path('all_posts', views.all_posts, name='all_posts'),  # All Posts page
]
