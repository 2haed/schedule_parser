from calendar_client import GoogleCalendar
from data.constants import exam_calendar, lecture_calendar, lab_calendar, consult_calendar, practical_calendar
import regex as re
import json


def load_schedule(filename: str) -> dict:
    with open(filename, 'r', encoding='utf-8') as json_file:
        schedule = json.load(json_file)
    return schedule


def upload_schedule(schedule: dict) -> None:
    for week_num, week in schedule.items():
        for day, pares in week.items():
            for time, pare in pares.items():
                date_time_start = '-'.join(day.split()[1].split('.')[::-1]) + 'T' + time.split()[2].split('-')[0] + ':00'
                date_time_end = '-'.join(day.split()[1].split('.')[::-1]) + 'T' + time.split()[2].split('-')[1] + ':00'
                location = ' '.join(pare.split()[-7:])
                summary = list(filter(None, re.split('(?=[А-Я])', ' '.join(pare.split()[:-7]))))
                obj = GoogleCalendar()
                event = {
                    'summary': summary[0],
                    'location': location if re.findall("\d+", location) != 2 else None,
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
                if event['description'] in ('Экзамен', 'Зачёт', 'Диф. зачет'):
                    event = obj.add_event(calendar_id=exam_calendar, body=event)
                elif event['description'] == 'Практическое занятие':
                    event = obj.add_event(calendar_id=practical_calendar, body=event)
                elif event['description'] == 'Лекция':
                    event = obj.add_event(calendar_id=lecture_calendar, body=event)
                elif event['description'] == 'Консультации':
                    event = obj.add_event(calendar_id=consult_calendar, body=event)
                elif event['description'] == 'Лабораторная работа':
                    event = obj.add_event(calendar_id=lab_calendar, body=event)


def main():
    upload_schedule(load_schedule(filename='data/data.json'))


if __name__ == '__main__':
    main()