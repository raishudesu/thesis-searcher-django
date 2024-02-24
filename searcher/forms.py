from django.forms import ModelForm
from django import forms
from .models import Comment, Thesis

class CommentForm(ModelForm):
    class Meta:
        model = Comment 
        fields = ['name', 'email', 'body']

class SearchForm(ModelForm):
    class Meta:
        model = Thesis
        fields = ['abstract']
        widgets = {'abstract': forms.TextInput(attrs={'size': 40}),}