from django.db import models


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    url = models.CharField(max_length=1000, null=True, blank=True)
    urlToImage = models.CharField(max_length=1000, null=True, blank=True)
    content = models.CharField(max_length=1000, null=True, blank=True)
    dateTime = models.DateTimeField(auto_now=True)

