import datetime
date1 = datetime.datetime(2025, 2, 11, 14, 19, 00)
date2 = datetime.datetime(2006, 12, 28, 17, 34, 00)
d = date1 - date2
print(d.total_seconds())