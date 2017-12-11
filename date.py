import datetime
day = 28
month = 2
year = 2000
print("Nam nay khong la nam nhuan") if year%4 else print("Nam nay la nam nhuan")
d = datetime.date(year, month, day)
# Ngay mai 
from datetime import datetime, timedelta
# add 1 day to d
d += timedelta(days = +1)
# Ngay
print(d.day)
# Thang 
print(d.month)
# Nam
print(d.year)
