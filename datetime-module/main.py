import datetime
a=datetime.datetime.now()
print(a)
b=datetime.datetime.now()
print(b.year)
print(b.month)
print('')
from datetime import datetime
import pytz
UTC=pytz.UTC
print(datetime.now(UTC))
KEL=pytz.timezone('Asia/Bahrain')
print(datetime.now(KEL))
print('')
data=datetime.now(KEL)
print('year is',data.year)
print('month is',data.month)
print('day is',data.day)
print('hour is',data.hour)
print('minute is',data.minute)
print('second is',data.second)
h=data.year
g=data.month
j=data.day
k=data.minute
e=data.hour
f=data.second
print('time is',e,':',k,':',f)#time
print('day is',j,':',g,':',h)#year
print('')#to get all the timezones in the world
for t in pytz.all_timezones:
    print(t)

