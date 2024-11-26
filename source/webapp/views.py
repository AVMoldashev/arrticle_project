from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from webapp.articleDB import ArticleDB
# Create your views here.


def index_view(request):
    context = {
        'articles': ArticleDB.articles
    }
    return render(request, 'index.html', context=context)


def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        article = {
            'title': request.POST.get('title'),
            'content': request.POST.get('content'),
            'author': request.POST.get('author')
        }
        ArticleDB.articles.append(article)
        return HttpResponseRedirect("/")

