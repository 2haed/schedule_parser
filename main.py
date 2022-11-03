from qparser import ScheduleParser, json_formatter, del_none
from calendar_client import GoogleCalendar
from constants import exam_calendar, lecture_calendar, lab_calendar, consult_calendar, practical_calendar
import regex as re
import sys


def main():
    group_name = input('Print group name to see schedule\nor -1 to exit: ')
    if group_name == str(-1):
        print('Bye!')
        sys.exit(0)
    else:
        with ScheduleParser() as parser:
            parser.get_schedule(group_name.lower())
            json_dict = del_none(json_formatter(parser.build_dataframe()))
            for key, val in json_dict.items():
                for k, v in val.items():
                    if v == 'Занятия отсутствуют':
                        continue
                    else:
                        date_time_start = key + 'T' + k.split()[0] + ':00'
                        date_time_end = key + 'T' + k.split()[1] + ':00'
                        location = ' '.join(v.split()[-7:])
                        summary = list(filter(None, re.split('(?=[А-Я])', ' '.join(v.split()[:-7]))))
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


if __name__ == '__main__':
    main()
