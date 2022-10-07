from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    name_scope = models.ManyToManyField('Tags', through='Scope',
                                        verbose_name='Тематика раздела', related_name='scopes')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tags(models.Model):

    name = models.CharField(max_length=50, verbose_name='Название раздела')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class Scope(models.Model):
    article_name = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Тематика', related_name='art_name')
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE, verbose_name="Название", related_name='tag')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        ordering = ('-is_main',)

