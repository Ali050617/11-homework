from django.db import models
from django.shortcuts import reverse
from datetime import date


class News(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.TextField()
    long_content = models.TextField()
    category = models.CharField(max_length=50)
    auther_name = models.CharField(max_length=50)
    date = models.DateField(default=date.today)

    class Meta:
        # verbose_name = 'News'
        verbose_name_plural = 'News'

    def get_detail_url(self):
        return reverse('news:detail', args=[self.pk])

