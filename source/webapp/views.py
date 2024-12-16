from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseNotFound
from webapp.forms import ArticleForm
from webapp.models import Article
from django.views.generic import View, TemplateView, FormView
# Create your views here.


class ArticleListView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'articles': Article.objects.all()
        }
        return render(request, 'index.html', context=context)


class ArticleCreateView(FormView):

    template_name = 'article_create.html'
    form_class = ArticleForm
    #success_url = reverse_lazy("articles")

    #def get(self, request, *args, **kwargs):
    #    form = ArticleForm()
    #    return render(request, 'article_create.html', {"form": form})

    def get_success_url(self):
        return reverse('article_detail', kwargs={"pk": self.article.pk})


    def form_valid(self, form):
        article = form.save()
        #article = Article.objects.create(title=form.cleaned_data['title'],
        #                                 content=form.cleaned_data['content'],
        #                                 author=form.cleaned_data['author']
        #                                 )
        #tags = form.cleaned_data['tags']
        #article.tags.set(tags)
        return redirect("article_detail", pk=article.pk) # super().form_valid(form)


    #def post(self, request, *args, **kwargs):
    #    form = ArticleForm(data=request.POST)
    #    if form.is_valid():
    #        article = Article.objects.create(title=form.cleaned_data['title'],
    #                                         content=form.cleaned_data['content'],
    #                                         author=form.cleaned_data['author']
    #                                         )
    #        tags = form.cleaned_data['tags']
    #        article.tags.set(tags)
    #        return redirect('article_detail', pk=article.id)
    #    else:
    #        return render(request, 'article_create.html', context={"form": form})


class ArticleView(TemplateView):
    template_name = 'article_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article"] = get_object_or_404(Article, pk=self.kwargs['pk'])
        return context


class ArticleUpdateView(FormView):
    template_name = 'article_update.html'
    form_class = ArticleForm

    def dispatch(self, request, *args, **kwargs):
        self.article = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = self.article
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs

    #def get_initial(self):
    #    return {'title': self.article.title,
    #            'content': self.article.content,
    #            'author': self.article.author,
    #            'tags': self.article.tags.all()
    #            }

    def form_valid(self, form):
        self.article = form.save()
        return redirect('article_detail', pk=self.article.id)
        #self.article.title = form.cleaned_data['title']
        #self.article.content = form.cleaned_data['content']
        #self.article.author = form.cleaned_data['author']
        #self.article.save()
        #tags = form.cleaned_data['tags']
        #self.article.tags.set(tags)
        #return redirect('article_detail', pk=self.article.id)

    #def get(self, request, *args, **kwargs):
    #    form = ArticleForm(initial={'title': self.article.title,
    #                                'content': self.article.content,
    #                                'author': self.article.author,
    #                                'tags': self.article.tags.all()
    #                                })
    #    return render(request, 'article_update.html', context={'form': form})

    #def post(self, request, *args, **kwargs):
    #    form = ArticleForm(data=request.POST)
    #    if form.is_valid():
    #        self.article.title = form.cleaned_data['title']
    #        self.article.content = form.cleaned_data['content']
    #        self.article.author = form.cleaned_data['author']
    #        self.article.save()
    #        tags = form.cleaned_data['tags']
    #        self.article.tags.set(tags)
    #        return redirect('article_detail', pk=self.article.id)
    #    else:
    #        return render(request, 'article_update.html', context={'form': form})


class ArticleDeleteView(View):
    def dispatch(self, request, *args, **kwargs):
        self.article = get_object_or_404(Article, pk=kwargs.get('pk'))
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'delete_article.html', context={"article": self.article})

    def post(self, request, *args, **kwargs):
        self.article.delete()
        return redirect('/')


