import datetime

def time(date1 ,date2):
    delta = date2 - date1
    if delta.days < 0:
        return abs(delta)
    return delta

date1 = datetime.date(2024, 4, 5)
date2 = datetime.date(2024, 8, 10)

print(time(date1, date2).days)