from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import sys
from constants import time
from dataclasses import dataclass


@dataclass
class ScheduleParser:
    URL = 'https://rasp.rea.ru/?q='
    OPTIONS = webdriver.ChromeOptions().add_argument('headless')
    SERVICE = Service('Wanderer.exe')
    driver: str
    schedule: str

    def get_schedule(self, group_name: str) -> None:
        self.driver.get('{}{}'.format(self.URL, group_name))
        self.driver.implicitly_wait(1)  # TODO: разобраться в wait
        try:
            if self.driver.find_element(By.CSS_SELECTOR, 'table'):
                self.schedule = self.driver.find_elements(By.CSS_SELECTOR, 'table')
        except Exception:
            print(self.driver.find_element(By.CSS_SELECTOR, 'h2').text,
                  self.driver.find_element(By.CSS_SELECTOR, 'h3').text, sep='\n')
            sys.exit(0)

    def get_info(self, finder) -> list:
        return [finder(table) for table in self.schedule]

    def build_dataframe(self) -> pd.DataFrame:
        dataframe = pd.DataFrame(index=time)
        lst = []
        new_schedule = []
        for pare in self.get_info(lambda x: x.find_elements(By.CLASS_NAME, 'slot')):
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
        for index, day in enumerate(self.get_info(lambda x: x.find_element(By.CSS_SELECTOR, 'h5').text.capitalize())):
            dataframe = dataframe.rename(columns={index: day})
        dataframe = dataframe.fillna('-')
        return dataframe

    def __enter__(self):
        self.driver = webdriver.Chrome(service=self.SERVICE, options=self.OPTIONS)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()
