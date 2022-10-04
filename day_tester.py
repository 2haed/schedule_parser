import re
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import unidecode


def remove_non_ascii(s):
    return re.sub(rb'[^\x00-\x7f]', rb' ', s.encode('utf8'))

group_name = '15.25Д-ЭКФ05/20б'
URL = 'https://rasp.rea.ru/?q='
OPTIONS = webdriver.ChromeOptions()
# OPTIONS.add_argument('headless')
SERVICE = Service('yandexdriver.exe')
driver = webdriver.Chrome(service=SERVICE, options=OPTIONS)
driver.get('{}{}'.format(URL, group_name.lower()))
driver.implicitly_wait(2)
# for i in range(1, 7):
#     days = driver.find_element(By.XPATH, f"/html/body/div[3]/div[3]/div[4]/div/div[{i}]").text.replace('\n', ' ')
#     print(days)

clicker = driver.find_element(By.CLASS_NAME, f"task")
clicker.click()
element = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[7]/div/div')
html = driver.page_source
soup = BeautifulSoup(html, features="html.parser")

continue_link = soup.find('div', class_='element-info-body').text
print(continue_link)
# modal = driver.find_element(By.CLASS_NAME, "modal-content")
# pares = modal.find_element(By.CSS_SELECTOR, 'a')
# print(pares.text)
driver.quit()