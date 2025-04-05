from django.core import validators
from django.db import models

# Create your models here.

from django.db import models
from django.db.models import CharField, BooleanField



class MyColorField(models.CharField):
    """ Поле для хранения HTML-кода цвета."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 7)
        super().__init__(*args, **kwargs)
        self.validators.append(validators.RegexValidator(r'#[a-f\d]{6}'))


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


class Socials(models.Model):
    title = CharField(max_length=100, verbose_name='Название', blank=True)
    logo = models.ImageField(upload_to='social_logos/', verbose_name='Логотип', blank=True)
    url_account = CharField(max_length=100, verbose_name='Ссылка на аккаунт', blank=True)
    enabled = BooleanField(default=True, verbose_name='Показывать на странице')


    def __str__(self):
        return self.url_account

    class Meta:
        verbose_name = 'Соцсеть'
        verbose_name_plural = ('Соцсети')

class Colors(models.Model):
    colortab1 = MyColorField(default='#ffffff', verbose_name='Цвета таблицы (ячейка 1-3)', blank=True)
    colortab2 = MyColorField(default='#ffffff', verbose_name='Цвета таблицы (ячейки 4,8,12,16,17)', blank=True)
    colortab3 = MyColorField(default='#ffffff', verbose_name='Цвета таблицы (ячейки 5-7,9-11,13-15)', blank=True)
    colorcards = MyColorField(default='#ffffff', verbose_name='Цвет карточек услуг', blank=True)
    colorlabels = MyColorField(default='#ffffff', verbose_name='Цвет названия и описания сайта', blank=True)
    coloredits = MyColorField(default='#ffffff', verbose_name='Цвет полей ввода', blank=True)


# class Fonts(models.Model):



# @receiver(pre_save, sender=Settings)
# def pr_save(sender, instance, **kwargs):
#     print("++++++++++++++++++++++++++++++ SAVE!!!!!!")
#
#     records = Settings.objects.filter(enabled=True)
#     if records:
#         for record in records:
#             record.enabled = False
#             record.save()

