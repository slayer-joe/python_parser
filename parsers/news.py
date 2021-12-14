from bs4 import BeautifulSoup as bs
import requests
from modules.BaseParser import BaseParser

class News(BaseParser):
    def __init__(self, url):
        self.url = url
        self.items_list = []
    
    def parse(self):
        response = requests.get(self.url)
        html = bs(response.content, 'html.parser')
        for el in html.select('.list-item__title'):
            self.items_list.append(el.text)
        return self.items_list



