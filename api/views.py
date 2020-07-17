from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from article.models import Article
from comment.models import Comment, AddComment
from django.http import JsonResponse


def get_article(req):
    article = Article.objects.all().values()
    article_list = list(article)
    return JsonResponse(article_list, safe=False)
