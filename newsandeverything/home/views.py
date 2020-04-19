from django.shortcuts import render, HttpResponse, get_object_or_404
from home.processNewsData import NewsData
from home.models import Foo
# Create your views here.

def home_page(request):
    # data = NewsData("in")
    # headline = data.get_news_data()
    # x = Foo(name="ulala")
    # x.save(force_insert=True)
    foo = Foo.objects.all()
    '''
    data from the models needs to be here
    '''
    print(len(foo))
    name = foo[0].name
    print(name)
    for i in range(len(foo)):
        print(foo[i].name)

    return HttpResponse(str(foo))