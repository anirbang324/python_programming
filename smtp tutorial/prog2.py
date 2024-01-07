import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)
my_dob = dt.datetime(year=1999, month= 5, day= 3)
print(my_dob)