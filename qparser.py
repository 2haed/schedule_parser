from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


URL = 'https://rasp.rea.ru/?q=15.01д-мфм01/20б'
options = webdriver.ChromeOptions()
s = Service('E:/CODES/GitHub/schedule_parser/yandexdriver.exe')
driver = webdriver.Chrome(service=s, options=options)
driver.get(URL)
driver.implicitly_wait(5)
schedule = driver.find_elements(By.CSS_SELECTOR, 'table')
days = []
time = set()
pares = []
for table in schedule:
    days.append(table.find_element(By.CSS_SELECTOR, 'h5').text.split(',')[0].capitalize())
    pares.append(table.find_elements(By.CLASS_NAME, 'slot'))
    for i in table.find_elements(By.CSS_SELECTOR, 'td'):
        time.add(' '.join(i.text.split()))

time.discard('')
time = set([x for x in time if len(x.split()) > 2])
new_set = set()
for i in time:
    if i[0].isdigit():
        new_set.add(i)
new_set.discard('1 пара')
time = list(sorted(new_set, key=lambda x: x[0]))
df = pd.DataFrame(index=time)
lst = []
new_schedule = []
for pare in pares:
    lst.append([x.text.strip().replace('\n', ' ') for x in pare])
for line in lst:
    new_schedule.append([(' '.join(x.split()[:4]),' '.join(x.split()[4:])) for x in line if len(x.split()) != 2])
for line in new_schedule:
    if not line:
        line.append(('1 пара 08:30 10:00', 'Занятия отсутствуют'))
for day, line in enumerate(new_schedule):
    idx, values = zip(*line)
    df.loc[list(idx), [day]] = pd.Series(values, list(idx))
for i, day in enumerate(days):
    df = df.rename(columns={i: day})
df = df.fillna('-')
print(df)
driver.quit()
