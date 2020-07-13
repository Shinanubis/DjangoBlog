from django.shortcuts import render
from comment.forms import AddComment


def addcomment(req):
    form = AddComment(req.POST or None)
    if form.is_valid():
        author = form.cleaned_data['author']
        content = form.cleaned_data['content']
        related_paper = form.cleaned_data['related_paper']
        created_at = form.cleaned_data['created_at']

        envoi = True

    return render(req, 'article/details.html', locals())
