import requests
from home.models import News


class NewsData:
    def __init__(self, api_url):
        self.api_url = api_url

    def request_google_news(self):
        google_news_response = requests.get(self.api_url)
        return google_news_response.json()

    def insert_data(self):
        News()

    def get_data(self):
        pass

