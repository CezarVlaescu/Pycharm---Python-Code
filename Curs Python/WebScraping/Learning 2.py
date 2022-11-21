import requests
import lxml
import bs4

result = requests.get('https://en.wikipedia.org/wiki/George_Washington')

soup = bs4.BeautifulSoup(result.text, 'lxml')

first_item = soup.select('.toctext')[0]
print(first_item.text)