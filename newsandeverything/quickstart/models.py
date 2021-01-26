from django.db import models

# Create your models here.


class NewsDetails(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.TextField(null=True, blank=True)
    urlToImage = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    dateTime = models.DateTimeField(auto_now=True)