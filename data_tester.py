import json
from typing import Union, Optional
import regex as re
import requests
from bs4 import BeautifulSoup
from data.constants import url, params, headers
import logging


logging.basicConfig(filename='errors.log', format='%(asctime)s %(message)s', encoding='utf-8', level=logging.WARNING)


def save_dict(dictionary: dict) -> tuple[bool, Union[Exception, None]]:
    try:
        with open('data/data.json', 'w', encoding='UTF-8') as json_file:
            json.dump(dictionary, json_file, indent=4, ensure_ascii=False)
    except FileNotFoundError as error:
        return False, error


def get_schedule() -> Optional[Union[Exception, dict]]:
    response_dict = {}
    for week_num in range(1,53):
        params['weekNum'] = str(week_num)
        try:
            response = requests.request("GET", url, headers=headers, params=params).text
            page = re.sub('<br/>', ' ', response)
            soup = BeautifulSoup(page, 'html.parser')
            for day in soup.find_all('div', class_='container'):
                date = day.find('th', class_='dayh').text
                for slot in day.find_all('tr', class_='slot'):
                    time = slot.find('td').text.strip()
                    if slot.find('span', class_='pcap'):
                        time = time[:6] + ' ' + time[6:11] + '-' + time[11:]
                    if slot.find('a', class_='task'):
                        pare = ' '.join(re.sub('\r\n', '', slot.find('a', class_='task').text).split())
                    else:
                        continue
                    response_dict[date + '.' + time] = pare
        except Exception as error:
            logging.warning(error)
            return error
    return response_dict


def main():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        save_dict(get_schedule())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()


if __name__ == '__main__':
    main()
