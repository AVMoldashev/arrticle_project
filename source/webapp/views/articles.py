from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.utils.http import urlencode

from webapp.forms import ArticleForm, SimpleSearchForm
from webapp.models import Article
from django.views.generic import View, TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
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


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm

    def get_success_url(self):
        return reverse('webapp:article_detail', kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        article = form.save()

        return redirect("webapp:article_detail", pk=article.pk)  # super().form_valid(form)


class ArticleView(DetailView):
    template_name = 'articles/article_view.html'
    model = Article
    context_object_name = "article"

    def get_context_object_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.order_by("created_at")  # self.get_object()
        return context


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "articles/article_update.html"
    form_class = ArticleForm


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "articles/delete_article.html"
    success_url = reverse_lazy("webapp:articles")
