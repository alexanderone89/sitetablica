from django.db import models

# Create your models here.

from django.db import models
from django.db.models import CharField


class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='Название')
    image = models.ImageField(upload_to="images/", verbose_name='Файл')
    enabled = models.BooleanField(default=True, verbose_name='Отображать на странице')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Settings(models.Model):
    theme = models.CharField(max_length=100, verbose_name='Тема', blank=True)
    nick = models.CharField(max_length=100, verbose_name='Ник', blank=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    logo = models.ImageField(upload_to='logos/', verbose_name='Логотип', blank=True)
    background = models.ImageField(upload_to='backgrounds/', verbose_name='Фон страницы', blank=True)
    enabled = models.BooleanField(default=True, verbose_name='Установить настройки')

    def __str__(self):
        return self.theme

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = ('Настройки')

class Servise(models.Model):
    title = CharField(max_length=100, verbose_name='Название', blank=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0, blank=True, verbose_name='Стоимость')
    enabled = models.BooleanField(default=True, verbose_name='Показывать на странице')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = ('Услуги')

# @receiver(pre_save, sender=Settings)
# def pr_save(sender, instance, **kwargs):
#     print("++++++++++++++++++++++++++++++ SAVE!!!!!!")
#
#     records = Settings.objects.filter(enabled=True)
#     if records:
#         for record in records:
#             record.enabled = False
#             record.save()