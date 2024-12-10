from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from webapp.forms import ArticleForm
from webapp.models import Article
from webapp.validate import article_validator
# Create your views here.


def index_view(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'index.html', context=context)


def article_create_view(request):
    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'article_create.html', {"form":form})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(title=form.cleaned_data['title'],
                                             content=form.cleaned_data['content'],
                                             author=form.cleaned_data['author'])
            return redirect('article_detail', pk=article.id)
        else:
            return render(request, 'article_create.html', context={"form":form})



def article_view(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_view.html', context={'article':article})



def article_update_view(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        form = ArticleForm(initial={'title': article.title,
                                    'content': article.content,
                                    'author': article.author})
        return render(request, 'article_update.html', context={'form':form})

    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.content = form.cleaned_data['content']
            article.author = form.cleaned_data['author']

            article.save()
            return redirect('article_detail', pk=article.id)
        else:
            return render(request, 'article_update.html', context={'form': form})


def delete_view(request, *args, pk, **kwargs):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_article.html')
    elif request.method == 'POST':
        article.delete()
        return redirect('/')


