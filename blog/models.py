from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    excerpt = models.CharField(max_length=255, blank=True, help_text="Short summary of the post.")
    featured_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    comments_count = models.PositiveIntegerField(default=0, editable=False)
    view_count = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user} bookmarked {self.post}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user} liked {self.post}"
