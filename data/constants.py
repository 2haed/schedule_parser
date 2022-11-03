time = ['08:30 10:00', '10:10 11:40', '11:50 13:20', '14:00 15:30', '15:40 17:10', '17:20 18:50', '18:55 20:25', '20:30 22:00']
exam_calendar = 'fc5964d829de9bcb88b1407d337b491608d779a412e63eaf342c531f3f1bb64c@group.calendar.google.com'
lecture_calendar = '38bdd2b020c1bd527628f975a6ec84bdd9edc61076d31adb3c347b33ebfb349b@group.calendar.google.com'
lab_calendar = '22566b311d8336c614da62210ade32650bcac4774f66ae23acba21b0412c6a18@group.calendar.google.com'
consult_calendar = '5bbb23ea64f80456fb760707752c52beae7c217258745cc06c78c5f999c8f530@group.calendar.google.com'
practical_calendar = '67b789fa5afaed6273860818ff9c7f5033aa662707f4d7aaf9c07a73e5ae6246@group.calendar.google.com'

url = "https://rasp.rea.ru/Schedule/ScheduleCard"
group_name = '15.25д-экф05/20б'.lower()
weekNum = ''
params = {'selection': group_name, 'weekNum': weekNum}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWJqZWN0Ijp7InVzZXJuYW1lIjoidXNlcm5hbWUiLCJyb2xlIjoidXNlciJ9LCJ0eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY2NzE0NDU4LCJpYXQiOjE2NjY3MTM1NTgsImp0aSI6IjExMjhiZjE0LTU3NzgtNDFiNy04MDk3LWVmZTI2NGRjYWQwNCJ9.n0bwfvZPoWiTS6bYKerGELridVD2ehdYGt2eFJ1bITU',
  'Accept': 'text/html, */*; q=0.01',
  'Referer': 'https://rasp.rea.ru/?q=15.25%D0%B4-%D1%8D%D0%BA%D1%8405%2F20%D0%B1',
  'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Yandex";v="22"',
  'sec-ch-ua-platfrom': '"Windows"',
  'X-Requested-With': 'XMLHttpRequest',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.4.863 Yowser/2.5 Safari/537.36'
}