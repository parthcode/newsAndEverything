from rest_framework import serializers
from quickstart.models import NewsDetails


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDetails
        fields = ['title', 'description', 'url', 'urlToImage', 'content', 'dateTime']
