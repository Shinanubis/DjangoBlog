from django import forms

class AddComment(forms.Form):
    author = forms.CharField(label='author', widget=forms.HiddenInput())
    related_paper = forms.CharField(label='related_paper', widget=forms.HiddenInput())
    content = forms.CharField(label='content', max_length=200, widget=forms.Textarea)
    created_at = forms.DateTimeField(widget=forms.HiddenInput())
