from typing import Optional, Union
from calendar_client import GoogleCalendar
from data.constants import calendars
import regex as re
import json


def load_schedule(filename: str) -> Optional[Union[Exception, dict]]:
    try:
        with open(filename, 'r', encoding='utf-8') as json_file:
            schedule = json.load(json_file)
    except FileNotFoundError as error:
        return error
    return schedule


def upload_schedule(schedule: dict) -> Optional[Union[Exception, None]]:
    for day, pares in schedule.items():
        try:
            date_time_start = "-".join(day.split('/')[0].split()[1].split('.')[::-1]) + 'T' + \
                              day.split('/')[1].split()[2].split('-')[0] + ':00'
            date_time_end = "-".join(day.split('/')[0].split()[1].split('.')[::-1]) + 'T' + \
                            day.split('/')[1].split()[2].split('-')[1] + ':00'
            location = ' '.join(pares.split()[-7:])
            summary = list(
                filter(None, re.split('(?=[А-Я])', ' '.join([i for i in pares.split()[:-6] if not i.isdigit()]))))
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
            obj = GoogleCalendar()
            if event['description'] in calendars:
                obj.add_event(calendar_id=calendars[event['description']], body=event)
        except Exception as ex:
            return ex


def main():
    upload_schedule(load_schedule(filename='data/data.json'))


if __name__ == '__main__':
    main()
