from django.db import models


class City(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название города')
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Название города'
        verbose_name_plural = 'Названия городов'

    def __str__(self):
        return self.name
