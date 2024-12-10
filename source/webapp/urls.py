from django.urls import path
from webapp.views import index_view, article_create_view, article_view, article_update_view,delete_view

urlpatterns = [
    path('', index_view, name="articles"),
    path('article/add/', article_create_view, name="create_article"),
    path('article/<int:pk>/', article_view, name="article_detail"),
    path('article/<int:pk>/update', article_update_view, name="update_article"),
    path('article/<int:pk>/delete', delete_view, name="delete")
]