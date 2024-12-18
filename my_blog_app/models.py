from django.db import models

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=40)
    
    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def get_full_name(self):
        return (f"{self.first_name} {self.last_name}")
    
    def __str__(self):
        return self.get_full_name()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title