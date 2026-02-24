from datetime import datetime

# Две даты
date1 = datetime(2026, 2, 20, 12, 0, 0)
date2 = datetime(2026, 2, 20, 14, 30, 0)

# Разница
delta = date2 - date1
seconds_difference = delta.total_seconds()

print("Difference in seconds:", seconds_difference)