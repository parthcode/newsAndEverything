from home.constant import HOMEURL, APIKEY, NEWS_KEYS
from home.models import Foo, Headlines
import requests

class NewsData:
    def __init__(self,country):
        self.country = country
        self.news_api = HOMEURL+self.country+APIKEY
        self.google_news_data = self.__get_google_news_data()

    def __get_google_news_data(self):
        data = requests.get(self.news_api)
        return data.json()
    #value='author','description','url','publishedAt','urlToImage'
    #'content'
    def get_news_data_json(self,value=None):
        length = len(self.google_news_data['articles'])
        news_data = []
        for i in range(length):
           data = self.google_news_data['articles'][i][value]
           news_data.append(data)
        return news_data

    def __insert_news_data(self):
        data = self.get_news_data_json(value=NEWS_KEYS[0])
        return data

    def fetch_news_data(self):
        print(self.__insert_news_data())

obj = NewsData("in")
print(obj.fetch_news_data())