from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from article.models import Article
from comment.models import Comment, AddComment
from django.http import JsonResponse


########### ARTICLE ############

##### GET ######
def get_article(req):
    article = Article.objects.all().values()
    article_list = list(article)
    return JsonResponse(article_list, safe=False)


def get_article_filter_by(req, article_id):
    article = Article.objects.filter(id=article_id).values()
    article_list = list(article)
    return JsonResponse(article_list, safe=False)


########### USER ##################

##### GET ######

def get_user(req):
    user = User.objects.all().values()
    user_list = list(user)
    return JsonResponse(user_list, safe=False)