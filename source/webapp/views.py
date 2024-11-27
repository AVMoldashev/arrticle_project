from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from webapp.models import Article
# Create your views here.


def index_view(request):
    context = {
        'articles': Article.objects.all()
    }
    return render(request, 'index.html', context=context)


def article_create_view(request):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        article = Article.objects.create(title=title, content=content, author=author)
        context = {
            'article': article
        }
        return render(request, 'article_view.html', context)

def article_view(request):
    article_id = request.GET.get('id')
    article = Article.objects.get(id=article_id)
    return render(request, 'article_view.html', context={'article': article})

