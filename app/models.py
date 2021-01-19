from django.db import models


class BlockHeadingModel(models.Model):
    title = models.CharField(verbose_name='Заголовок страницы', max_length=256)
    description = models.TextField(verbose_name='Описание страницы', blank=True)
    buttonText = models.TextField(verbose_name='Текст кнопки')
    img = models.CharField(verbose_name='Фоновое изображение', blank=True, default='', max_length=400)
    background_color = models.CharField(verbose_name='Цвет фона', max_length=7, default='#ebebeb')


class BlockSectionModel(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=256, blank=True)
    subtitle = models.CharField(verbose_name='Подзаголовок', max_length=256, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    img = models.CharField(verbose_name='Фоновое изображение', blank=True, default='', max_length=400)
    background_color = models.CharField(verbose_name='Цвет фона', max_length=7, default='#ebebeb')


class BlockTextModel(models.Model):
    text = models.TextField(verbose_name='Текст', blank=True)
    img = models.CharField(verbose_name='Фоновое изображение', blank=True, default='', max_length=400)
    background_color = models.CharField(verbose_name='Цвет фона', max_length=7, default='#ebebeb')


class BlockFormModel(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=256, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    buttonText = models.TextField(verbose_name='Текст кнопки')
    text = models.TextField(verbose_name='Текст под формой', blank=True)
    img = models.CharField(verbose_name='Фоновое изображение', blank=True, default='', max_length=400)
    background_color = models.CharField(verbose_name='Цвет фона', max_length=7, default='#ebebeb')
