from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from article.models import Article
from django.forms import ModelForm


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    related_paper = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(editable=False)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        return super(Comment, self).save(*args, **kwargs)


class AddComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'related_paper', 'author']
