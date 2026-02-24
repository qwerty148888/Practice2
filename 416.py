from datetime import datetime, timedelta, timezone

# Функция для парсинга даты с временем и смещением
def parse_datetime(s):
    # Разделяем на дату-время и смещение
    dt_str, tz_str = s.split(' UTC')
    
    # Парсим дату и время
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    
    # Парсим смещение
    sign = 1 if tz_str[0] == '+' else -1
    hours = int(tz_str[1:3])
    minutes = int(tz_str[4:6])
    
    offset = timedelta(hours=hours, minutes=minutes) * sign
    
    # Возвращаем datetime с информацией о часовом поясе
    return dt.replace(tzinfo=timezone(offset))

# Читаем входные данные
start = parse_datetime(input())
end = parse_datetime(input())

# Переводим в UTC и считаем разницу
duration_seconds = int((end.astimezone(timezone.utc) - start.astimezone(timezone.utc)).total_seconds())

print(duration_seconds)