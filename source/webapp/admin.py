from django.contrib import admin
# Register your models here.

from webapp.models import Article, Tag, Comment#, ArticleTag

class TagInline(admin.TabularInline):
    model = Article.tags.through


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at']
    list_display_links = ['id', 'title']
    list_filter = ['author']
    search_fields = ['title', 'content']
    fields = ['title', 'author', 'content', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [TagInline]

admin.site.register(Tag)
admin.site.register(Comment)
#admin.site.register(ArticleTag)