from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.TextField()
    long_content = models.TextField()
    category = models.CharField(max_length=50)

    class Meta:
        # verbose_name = 'News'
        verbose_name_plural = 'News'