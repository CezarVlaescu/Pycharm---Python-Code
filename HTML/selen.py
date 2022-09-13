from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)
browser.get('https://www.emag.ro/')
get_element = browser.find_element(by=By.ID, value='searchboxTrigger')
get_element.send_keys('iphone 13')
get_element.submit()

# find_element = browser.find_element(by=By.ID, value='card_grid')
# print(find_element.text.split('\n'))

# for i in range(1,61):
#     find_element = browser.find_element(by=By.XPATH, value=f'//*[@id="card_grid"]/div[{i}]')
#     print(find_element.text)
#     print('*********************')


