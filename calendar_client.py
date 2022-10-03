from google.oauth2 import service_account
from googleapiclient.discovery import build
import pprint


class GoogleCalendar:
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    FILE_PATH = 'calendar_client.json'

    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(
            filename=self.FILE_PATH, scopes=self.SCOPES
        )
        self.service = build('calendar', 'v3', credentials=credentials)

    def get_calendar_list(self):
        return self.service.calendarList().list().execute()

    def add_calendar(self, calendar_id):
        calendar_list_entry = {
            'id' : calendar_id
        }
        return self.service.calendarList().insert(body=calendar_list_entry).execute()

    def add_event(self, calendar_id, body):
        return self.service.events().insert(calendarId=calendar_id, body=body).execute()


obj = GoogleCalendar()
calendar = '5bbb23ea64f80456fb760707752c52beae7c217258745cc06c78c5f999c8f530@group.calendar.google.com'
# pprint.pprint(obj.get_calendar_list())

event = {
  'summary': 'Тестовый ивент',
  'location': 'Рэу',
  'description': 'Тестовое описание',
  'start': {
    'date': '2022-10-04',
  },
  'end': {
    'date': '2022-10-04',
  },
}

event = obj.add_event(calendar_id=calendar, body=event)