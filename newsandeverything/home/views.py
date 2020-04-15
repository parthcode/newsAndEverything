from django.shortcuts import render, HttpResponse
from home.processNewsData import NewsData
from home.models import News
# Create your views here.

def home_page(request):
    # data = NewsData("in")
    # headline = data.get_news_data()
    data = News(title='Something', author='firstRow')
    data.save()
    foo = News.objects.all()
    return HttpResponse(str(headline))