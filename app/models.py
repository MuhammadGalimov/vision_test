from django.db import models
from django.core.validators import RegexValidator


class BlockHeadingModel(models.Model):
    title = models.CharField(verbose_name='Заголовок страницы', max_length=256)
    description = models.TextField(verbose_name='Описание страницы', blank=True)
    buttonText = models.TextField(verbose_name='Текст кнопки')
    img = models.URLField(verbose_name='Фоновое изображение', blank=True, default='', max_length=400)
    background_color = models.CharField(verbose_name='Цвет фона', max_length=7, default='#ebebeb')


class BlockSectionModel(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=256, blank=True)
    subtitle = models.CharField(verbose_name='Подзаголовок', max_length=256, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    img = models.URLField(verbose_name='Фоновое изображение', blank=True, default='', max_length=400)
    background_color = models.CharField(verbose_name='Цвет фона', max_length=7, default='#ebebeb')


class BlockTextModel(models.Model):
    text = models.TextField(verbose_name='Текст', blank=True)
    img = models.URLField(verbose_name='Фоновое изображение', blank=True, default='', max_length=400)
    background_color = models.CharField(verbose_name='Цвет фона', max_length=7, default='#ebebeb')


class BlockFormModel(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=256, blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    buttonText = models.TextField(verbose_name='Текст кнопки')
    text = models.TextField(verbose_name='Текст под формой', blank=True)
    img = models.URLField(verbose_name='Фоновое изображение', blank=True, default='', max_length=400)
    background_color = models.CharField(verbose_name='Цвет фона', max_length=7, default='#ebebeb')


class MailsModel(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?\d{11}$')
    phone = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    text = models.TextField(blank=True)


# class BlockOrd(models.Model):
#    heading_id = models.OneToOneField(BlockHeadingModel, on_delete=models.CASCADE)
