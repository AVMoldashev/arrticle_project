from django import forms
from django.forms import widgets

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Название")
    content = forms.CharField( required=True, label="Текст", widget=widgets.Textarea)
    author = forms.CharField(max_length=50, required=True, label="Автор")