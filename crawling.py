import requests
from bs4 import BeautifulSoup


def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html




URL = "http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=tue&page=1"
html = get_html(URL)
soup = BeautifulSoup(html, 'html.parser')
