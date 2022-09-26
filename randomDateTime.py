from random import randrange
from datetime import timedelta
from datetime import datetime

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

def get_dates():
    d1 = datetime.strptime('1/1/2005 1:30 PM', '%m/%d/%Y %I:%M %p')
    date1 = random_date(d1, datetime.now())
    date2 = random_date(d1, datetime.now())
    dif = date1 - date2
    if dif > timedelta(0):
        return [date2.isoformat('T'), date1.isoformat('T')]
    else:
        return [date1.isoformat('T'), date2.isoformat('T')]