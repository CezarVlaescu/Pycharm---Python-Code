import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
browser.get('https://www.emag.ro/#opensearch')
get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
get_element.send_keys('telefon')
get_element.submit()

url= requests.get(browser.current_url)
page = BeautifulSoup(url.text, 'html.parser')
print(page)
data = {}
counter = 1
for i in page.find_all('div', attrs={'class':'card-v2-wrapper'}):
    # print(i)
    product_name = i.find('a', attrs={'class':'card-v2-title'}).get_text()
    rating_number = i.find('span', attrs={'class':'average-rating'}).get_text()
    reviews_number = int(i.find('span', attrs={'class': 'visible-xs-inline-block'}).get_text().replace('(','').replace(')', ''))
    price = float(i.find('p', attrs={'class': 'product-new-price'}).get_text().replace('Lei','').replace('.','').replace(',','.'))
    data[f"product_{counter}"] = {'product_name': product_name, 'rating_number': rating_number,
                                  'reviews_number': reviews_number, 'price': price}
    counter =+ 1
    print(data,'30')

    # print(type(data))

export_data = pd.DataFrame(data).transpose().to_csv('Telefoane.csv',sep=',', header=['Product_number','Rating_number','Reviews_number' , 'Price'])
