from django.urls import path
from webapp.views.articles import ArticleListView,ArticleCreateView,ArticleView, ArticleUpdateView,ArticleDeleteView

urlpatterns = [
    path('', ArticleListView.as_view(), name="articles"),
    path('article/add/', ArticleCreateView.as_view(), name="create_article"),
    path('article/<int:pk>/', ArticleView.as_view(), name="article_detail"),
    path('article/<int:pk>/update', ArticleUpdateView.as_view(), name="update_article"),
    path('article/<int:pk>/delete', ArticleDeleteView.as_view(), name="delete")
]