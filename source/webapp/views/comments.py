from django.views.generic import CreateView, UpdateView, DeleteView
from webapp.models import Comment, Article
from webapp.forms import CommentForm
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect


class CommentsCreateView(CreateView):
    model = Comment
    template_name = "comments/comment_create.html"
    form_class = CommentForm

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        form.instance.article = article
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('webapp:article_detail', kwargs={"pk": self.object.article.pk})


class CommentUpdateView(UpdateView):
    model = Comment
    template_name = "comments/comment_update.html"
    form_class = CommentForm

    def get_success_url(self):
        return reverse('webapp:article_detail', kwargs={"pk": self.object.article.pk})

class CommentDeleteView(DeleteView):
    model = Comment

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect("webapp:article_detail", pk=self.object.article.pk)




