from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.utils.http import urlencode

from webapp.forms import ArticleForm, SimpleSearchForm
from webapp.models import Article
from django.views.generic import View, TemplateView, FormView, ListView
from django.db.models import Q


# Create your views here.


class ArticleListView(ListView):  # View

    model = Article
    template_name = 'articles/index.html'
    context_object_name = "articles"
    ordering = ["-created_at"]
    is_paginated = True
    paginate_by = 3
    paginate_orphans = 1

    def dispatch(self, request, *args, **kwargs):
        self.search_form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.search_form.is_valid():
            return self.search_form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(title__icontains=self.search_value) | Q(author__icontains=self.search_value))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # super(ArticleListView, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form
        if self.search_value:
            context["query"] = urlencode({"search": self.search_value})
            context["search_value"] = self.search_value
        return context




class ArticleCreateView(FormView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm


    def get_success_url(self):
        return reverse('article_detail', kwargs={"pk": self.article.pk})

    def form_valid(self, form):
        article = form.save()
        # article = Article.objects.create(title=form.cleaned_data['title'],
        #                                 content=form.cleaned_data['content'],
        #                                 author=form.cleaned_data['author']
        #                                 )
        # tags = form.cleaned_data['tags']
        # article.tags.set(tags)
        return redirect("article_detail", pk=article.pk)  # super().form_valid(form)

    # def post(self, request, *args, **kwargs):
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
    template_name = 'articles/article_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article"] = get_object_or_404(Article, pk=self.kwargs['pk'])
        return context


class ArticleUpdateView(FormView):
    template_name = 'articles/article_update.html'
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

    # def get_initial(self):
    #    return {'title': self.article.title,
    #            'content': self.article.content,
    #            'author': self.article.author,
    #            'tags': self.article.tags.all()
    #            }

    def form_valid(self, form):
        self.article = form.save()
        return redirect('article_detail', pk=self.article.id)
        # self.article.title = form.cleaned_data['title']
        # self.article.content = form.cleaned_data['content']
        # self.article.author = form.cleaned_data['author']
        # self.article.save()
        # tags = form.cleaned_data['tags']
        # self.article.tags.set(tags)
        # return redirect('article_detail', pk=self.article.id)

    # def get(self, request, *args, **kwargs):
    #    form = ArticleForm(initial={'title': self.article.title,
    #                                'content': self.article.content,
    #                                'author': self.article.author,
    #                                'tags': self.article.tags.all()
    #                                })
    #    return render(request, 'article_update.html', context={'form': form})

    # def post(self, request, *args, **kwargs):
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
        return render(request, 'articles/delete_article.html', context={"article": self.article})

    def post(self, request, *args, **kwargs):
        self.article.delete()
        return redirect('/')
