from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponseNotFound
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
        return redirect('article_detail', pk=article.id)
        #url = reverse('article_detail', kwargs={'pk':article.id})
        #return HttpResponseRedirect(url)



def article_view(request, *args, pk, **kwargs):
    #print(args, kwargs)
    #article_id = request.GET.get('id')
    #try:
    #    article = Article.objects.get(id=pk)
    #except Article.DoesNotExist:
    #    return HttpResponseNotFound('Article not Found')
    #    raise Http404
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_view.html', context={'article':article})


