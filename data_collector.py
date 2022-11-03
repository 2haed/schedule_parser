import json
import regex as re
import requests
from bs4 import BeautifulSoup
from data.constants import url, params, headers


def save_dict(dictionary: dict) -> None:
    with open('data/data.json', 'w', encoding='UTF-8') as json_file:
        json.dump(dictionary, json_file, indent=4, ensure_ascii=False)


def get_schedule() -> dict:
    response_dict = {}
    for week_num in range(1, 53):
        params['weekNum'] = str(week_num)
        response = requests.request("GET", url, headers=headers, params=params).text
        page = re.sub('<br/>', ' ', response)
        soup = BeautifulSoup(page, 'html.parser')
        week_dict = {}
        for day in soup.find_all('div', class_='container'):
            date = day.find('th', class_='dayh').text
            day_dict = {}
            for slot in day.find_all('tr', class_='slot'):
                time = slot.find('td').text.strip()
                if slot.find('span', class_='pcap'):
                    time = time[:6] + ' ' + time[6:11] + '-' + time[11:]
                if slot.find('a', class_='task'):
                    pare = ' '.join(re.sub('\r\n', '', slot.find('a', class_='task').text).split())
                else:
                    continue
                day_dict[time] = pare
            if day_dict:
                week_dict[date] = day_dict
            else:
                pass
        if week_dict:
            response_dict[f'{week_num} Неделя'] = week_dict
        else:
            pass
    return response_dict


def main():
    save_dict(get_schedule())


if __name__ == '__main__':
    main()