import requests
import lxml
from bs4 import BeautifulSoup
import chardet

result = requests.get("https://ro.wikipedia.org/wiki/Omul-p%C4%83ianjen_3")

soup = BeautifulSoup(result.text, lxml)
print(soup)
