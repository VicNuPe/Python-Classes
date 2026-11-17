'''from datetime import date, time, datetime, timedelta, timezone

print(date.today())
print(datetime.now())
print(timedelta(days=3, hours=2))'''
""" 
from datetime import datetime, timezone

local = datetime.now().astimezone()
utc = local.astimezone(timezone.utc)

print("Local:", local.isoformat())
print("UTC: ", utc.isoformat())
print("Same instant?", local == utc) """

""" from datetime import datetime

text = "2026-12-31 23:59"
try:
    result = datetime.strptime(text, "%Y-%m-%d %H:%M")
    print("Parsed:", result)
except ValueError:
    print("Invalid date or time") """

# print("Invalid date or time")
""" 
from datetime import datetime, timedelta

start = datetime(2026, 11, 2, 9, 0)
duration = timedelta(days=2, hours=3, minutes=30)
deadline = start + duration

print(deadline.strftime("%d/%m/%Y %H:%M"))
# 04/11/2026 12:30 """

""" from datetime import date[cite: 5]


start = date(2026, 12, 24)[cite: 5]
end = date(2026, 12, 25)[cite: 5]

difference = end - start[cite: 5]
print(difference)      # 1 day, 0:00:00[cite: 5]
print(difference.days) # 1[cite: 5] """

