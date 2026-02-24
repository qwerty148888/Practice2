from datetime import datetime, timedelta, timezone

def parse_datetime(s):
    # Разделяем дату и смещение
    date_str, tz_str = s.split()
    
    # Парсим дату
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Парсим смещение
    sign = 1 if tz_str[3] == '+' else -1
    hours = int(tz_str[4:6])
    minutes = int(tz_str[7:9])
    offset = timedelta(hours=hours, minutes=minutes) * sign
    
    # Возвращаем datetime с UTC смещением
    return dt.replace(tzinfo=timezone(offset))

# Читаем две даты
a = parse_datetime(input())
b = parse_datetime(input())

# Разница в днях
diff_seconds = abs((a - b).total_seconds())
full_days = int(diff_seconds // 86400)  # 86400 секунд в дне

print(full_days)