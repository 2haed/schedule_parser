import requests
from bs4 import BeautifulSoup
import urllib.parse


URL = 'https://rasp.rea.ru/?q=15.25д-экф05%2F20б'

string = urllib.parse.unquote(URL, encoding='utf-8')
print(string)

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36 '
}
html = requests.get(string)
print(html)
soup = BeautifulSoup(html.text, 'html.parser')
items = soup.find('h2').get_text()
print(items)


# cards = []
# for item in items:
#     print(item)
#     cards.append(
#         {
#             'number': item.find('span', class_='pcap')
#         }
#     )
# print(cards)