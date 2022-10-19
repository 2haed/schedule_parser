from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


group_name = '15.25Д-ЭКФ05/20б'
URL = 'https://rasp.rea.ru/?q='
OPTIONS = webdriver.ChromeOptions()
# OPTIONS.add_argument('headless')
SERVICE = Service('yandexdriver.exe')
driver = webdriver.Chrome(service=SERVICE, options=OPTIONS)
driver.get('{}{}'.format(URL, group_name.lower()))
driver.implicitly_wait(5)
clicker = driver.find_element(By.CLASS_NAME, f"slot")
clicker.click()
data_group = driver.find_element(By.CLASS_NAME, 'element-info-body').text.split('\n')
print(data_group)
# data = data_group.find_element(By.CSS_SELECTOR, 'h5').text
# print(data)