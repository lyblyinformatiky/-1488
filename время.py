from datetime import datetime as dt
import datetime as tm
now = dt.now() + tm.timedelta(hours = 10)
week = dt.today().weekday()
datetime = now.strftime('%d.%m.%Y')
Time = now.strftime('%H:%M')
a = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресение']
print(f"медный бычок 1488")
print(f'Сегодня {a[week]}, сейчас {Time}. Дата:{datetime}')
