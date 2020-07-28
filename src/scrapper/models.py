from django.db import models
from scrapper.utils import from_cyrillic_to_eng
import jsonfield


def default_urls():
    return {'work': '', 'rabota': '', 'dou': '', 'djinni': ''}


class City(models.Model):
    name = models.CharField(
        max_length=20, verbose_name='Название города', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Название города'
        verbose_name_plural = 'Названия городов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(
        max_length=20, verbose_name='Язык программирования', unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Jobs(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Вакансия')
    company = models.CharField(max_length=250, verbose_name='Компания')
    description = models.TextField(verbose_name='Описание')
    city = models.ForeignKey(
        'City', on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey(
        'Language', on_delete=models.CASCADE, verbose_name='Язык программирования')
    time_stamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        ordering = ['-time_stamp']

    def __str__(self):
        return self.title


class Error(models.Model):
    time_stamp = models.DateField(auto_now_add=True)
    data = jsonfield.JSONField()


class Url(models.Model):
    city = models.ForeignKey(
        'City', on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey(
        'Language', on_delete=models.CASCADE, verbose_name='Язык программирования')
    url_data = jsonfield.JSONField(default=default_urls)

    class Meta:
        unique_together = ('city', 'language')
