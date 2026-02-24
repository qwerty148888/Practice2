from datetime import datetime, timedelta

# Текущая дата и время
now = datetime.now()

# Вычитаем 5 дней
five_days_ago = now - timedelta(days=5)

print("Current date:", now)
print("Date 5 days ago:", five_days_ago)