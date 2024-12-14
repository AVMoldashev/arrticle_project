from django.urls import path
from webapp.views import ArticleListView,ArticleCreateView,ArticleView, ArticleUpdateView,ArticleDeleteView

urlpatterns = [
    path('', ArticleListView, name="articles"),
    path('article/add/', ArticleCreateView, name="create_article"),
    path('article/<int:pk>/', ArticleView, name="article_detail"),
    path('article/<int:pk>/update', ArticleUpdateView, name="update_article"),
    path('article/<int:pk>/delete', ArticleDeleteView, name="delete")
]