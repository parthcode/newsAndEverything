from django.db import models
from django.utils import timezone

class Headlines(models.Model):
    title = models.TextField()
    published_date = models.DateTimeField(default=timezone.now())
    content = models.TextField()
    url_to_image = models.TextField()
    news_url = models.CharField(max_length=1000)
    author = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Foo(models.Model):
    name = models.CharField(max_length=100)
