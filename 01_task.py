import datetime

def get_days_from_today(date):
    now=datetime.datetime.now()
    date=datetime.datetime.strptime(date, "%Y-%m-%d")
    result = (now - date).days
    return result
 
print(get_days_from_today("2022-01-01"))
print(get_days_from_today("2028-01-01"))
print(get_days_from_today("2024-11-18"))
