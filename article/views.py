from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from .models import Article
from comment.models import Comment, AddComment


def index(req):
    article_list = Article.objects.order_by('-created_at')[:5]
    context = {'article_list': article_list}
    return render(req, 'article/index.html', context)


def detail(req, article_id):
    article = get_object_or_404(Article, pk=article_id)
    form = AddComment(initial={
                                'author': getattr(User.objects.first(), 'username'),
                                'related_paper': getattr(article, 'title')
                              }, auto_id=False)
    if req.method == 'POST':
        form = AddComment(req.POST or None)
        if form.is_valid():
            form.save()
            form = AddComment
    comments_list = Comment.objects.order_by('-created_at')
    context = {'article': article, 'comments_list': comments_list, 'form': form}
    return render(req, 'article/details.html', context)
