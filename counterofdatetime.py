from datetime import date
from datetime import timedelta

y, m, d = input().split()
ny_date = date(int(y), int(m), int(d))
delta = timedelta(int(input()))

ny_date = ny_date + delta
print(ny_date.year, ny_date.month, ny_date.day)
