from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    class Meta:
        abstract = True


class Article(BaseModel):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    author = models.CharField(max_length=50, null=False, blank=False, verbose_name="Автор")
    content = models.TextField(null=False, blank=False, verbose_name="Контент")
    tags = models.ManyToManyField('webapp.Tag', related_name='articles', blank=True)
    #tags_old = models.ManyToManyField('webapp.Tag',
    #                              related_name='articles_old',
    #                              through='webapp.ArticleTag',
    #                              through_fields=('article', 'tag'),
    #                              blank=True)



    def __str__(self):
        return f'{self.id}. {self.title}'

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(BaseModel):
   article = models.ForeignKey('webapp.Article', related_name='comments', on_delete=models.CASCADE, verbose_name='Статья')
   text = models.TextField(max_length=400, verbose_name='Комментарий')
   author = models.CharField(max_length=40, null=True, blank=True, default='Аноним', verbose_name='Автор')


   def __str__(self):
       return self.text[:20]

   class Meta:
       db_table = 'comments'
       verbose_name = 'Комментарий'
       verbose_name_plural = 'Комментарии'


class Tag(BaseModel):
    name = models.CharField(max_length=31, verbose_name='Тег', unique=True)



    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


#class ArticleTag(BaseModel):
#    article = models.ForeignKey('webapp.Article', related_name='article_tags', on_delete=models.CASCADE, verbose_name='Статья')
#    tag = models.ForeignKey('webapp.Tag', related_name='tag_articles', on_delete=models.CASCADE, verbose_name='Тег')
#
#
#    def __str__(self):
#        return f"{self.article} | {self.tag}"

