from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import sys
from constants import time


class ScheduleParser:
    URL = 'https://rasp.rea.ru/?q='
    OPTIONS = webdriver.ChromeOptions()
    SERVICE = Service('yandexdriver.exe')

    def __init__(self, group_name):
        self.driver = webdriver.Chrome(service=self.SERVICE, options=self.OPTIONS)
        self.group_name = group_name

    def get_schedule(self):
        self.driver.get('{}{}'.format(self.URL, self.group_name))
        self.driver.implicitly_wait(1)
        try:
            if self.driver.find_element(By.CSS_SELECTOR, 'table'):
                schedule = self.driver.find_elements(By.CSS_SELECTOR, 'table')
                return schedule
        except Exception:
            print(self.driver.find_element(By.CSS_SELECTOR, 'h2').text, self.driver.find_element(By.CSS_SELECTOR, 'h3').text, sep='\n')
            self.driver.quit()
            sys.exit(0)
        self.driver.quit()

    def get_days(self):
        days = []
        schedule = self.get_schedule()
        for table in schedule:
            days.append(table.find_element(By.CSS_SELECTOR, 'h5').text.capitalize())
        return days

    def get_pares(self):
        pares = []
        schedule = self.get_schedule()
        for table in schedule:
            pares.append(table.find_elements(By.CLASS_NAME, 'slot'))
        return pares

    def build_dataframe(self):
        dataframe = pd.DataFrame(index=time)
        lst = []
        new_schedule = []
        for pare in self.get_pares():
            lst.append([x.text.strip().replace('\n', ' ') for x in pare])
        for line in lst:
            new_schedule.append(
                [(' '.join(x.split()[:4]), ' '.join(x.split()[4:])) for x in line if len(x.split()) != 2])
        for line in new_schedule:
            if not line:
                line.append(('1 пара 08:30 10:00', 'Занятия отсутствуют'))
        for day, line in enumerate(new_schedule):
            idx, values = zip(*line)
            dataframe.loc[list(idx), [day]] = pd.Series(values, list(idx))
        for index, day in enumerate(self.get_days()):
            dataframe = dataframe.rename(columns={index: day})
        dataframe = dataframe.fillna('-')
        self.driver.quit()
        return dataframe
