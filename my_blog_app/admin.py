from django.contrib import admin
from .models import Post, Author, Tag, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "author", "date")
    prepopulated_fields = {"slug":("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_filter = ("user_name", "post", "date",)
    list_display = ("user_name", "post", "date")

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)