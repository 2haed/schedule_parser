import json
import regex as re
from typing import Optional, Union

from google.protobuf import service
from googleapiclient.http import BatchHttpRequest
import httplib2
from googleapiclient import discovery

from data.constants import lab_calendar


def load_schedule(filename: str) -> Optional[Union[Exception, dict]]:
    try:
        with open(filename, 'r', encoding='utf-8') as json_file:
            schedule = json.load(json_file)
    except FileNotFoundError as error:
        return error
    return schedule


schedule = load_schedule('data/data.json')
for day, pares in schedule.items():
    try:
        date_time_start = "-".join(day.split('/')[0].split()[1].split('.')[::-1]) + 'T' + day.split('/')[1].split()[2].split('-')[0] + ':00'
        date_time_end = "-".join(day.split('/')[0].split()[1].split('.')[::-1]) + 'T' + day.split('/')[1].split()[2].split('-')[1] + ':00'
        location = ' '.join(pares.split()[-7:])
        summary = list(filter(None, re.split('(?=[А-Я])', ' '.join([i for i in pares.split()[:-6] if not i.isdigit()]))))
        event = {
            'summary': summary[0],
            'location': location if re.findall(r'\d+', location) else None,
            'description': summary[1] if not len(summary) == 1 else None,
            'start': {
                'dateTime': date_time_start,
                'timeZone': 'Europe/Moscow'
            },
            'end': {
                'dateTime': date_time_end,
                'timeZone': 'Europe/Moscow'
            },
        }
    except Exception as ex:
        raise ex
