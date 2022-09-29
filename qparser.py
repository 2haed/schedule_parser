from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


URL = 'https://rasp.rea.ru/?q=15.25д-экф05%2F20б'
options = webdriver.ChromeOptions()
s = Service('E:/CODES/GitHub/schedule_parser/yandexdriver.exe')
driver = webdriver.Chrome(service=s, options=options)
driver.get(URL)
schedule = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[4]/div/div[1]/div/table/tbody/tr[1]/td[2]/a/text()[2]')
print(schedule.text)

# print(element.get_text())
# driver.quit()