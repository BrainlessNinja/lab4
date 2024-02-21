import datetime as dt
date = dt.datetime.now()
delta = dt.timedelta(days=1)
tomorrow = date + delta
yesterday = date - delta
print(yesterday)
print(date)
print(tomorrow)