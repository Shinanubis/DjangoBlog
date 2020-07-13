from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    author = models.ForeignKey(User, on_delete=False)
    category = models.ForeignKey(Category, on_delete=False)
    content = models.TextField()
    created_at = models.DateTimeField(editable=False)
    edited_at = models.DateTimeField('edited date', null=True, blank=True)
    published_at = models.DateTimeField('published date', null=True, blank=True)
    cover = models.ImageField(upload_to='article/img/cover', null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Article, self).save(*args, **kwargs)
