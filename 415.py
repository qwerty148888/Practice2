from datetime import datetime, timedelta, timezone
import math

def parse_date(s):
    date_str, tz_str = s.split()
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    sign = 1 if tz_str[3] == '+' else -1
    hours = int(tz_str[4:6])
    minutes = int(tz_str[7:9])
    offset = timedelta(hours=hours, minutes=minutes) * sign
    return dt.replace(tzinfo=timezone(offset))

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

birth = parse_date(input())
current = parse_date(input())

month = birth.month
day = birth.day
year = current.year

# Обработка 29 февраля
if month == 2 and day == 29 and not is_leap(year):
    day = 28

# Создаём дату следующего дня рождения в текущем году
next_birthday = datetime(year, month, day, tzinfo=birth.tzinfo)

# Если уже прошла, берём следующий год
if next_birthday.astimezone(timezone.utc) < current.astimezone(timezone.utc):
    year += 1
    if month == 2 and birth.day == 29 and not is_leap(year):
        day = 28
    else:
        day = birth.day
    next_birthday = datetime(year, month, day, tzinfo=birth.tzinfo)

# Разница в секундах по UTC
diff_seconds = (next_birthday.astimezone(timezone.utc) - current.astimezone(timezone.utc)).total_seconds()

# Считаем дни с округлением вверх
days_left = math.ceil(diff_seconds / 86400)

print(days_left)