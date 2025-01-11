from django.db import models

# Create your models here.

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='Название')
    image = models.ImageField(upload_to="images/", verbose_name='Файл')
    enabled = models.BooleanField(default=True, verbose_name='Отображать на странице')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
