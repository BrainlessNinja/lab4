import datetime as dt

date1 = dt.datetime.now()
date2 = dt.datetime(2018,5,7)

delta = date1 - date2
print(delta.total_seconds())