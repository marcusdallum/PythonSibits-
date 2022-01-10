import datetime
from dateutil.relativedelta import relativedelta

date = datetime.datetime.now()
justdate = date.strftime("%x")
justtime = date.strftime("%X")

print(date)
print(justdate)
print(justtime)

date = datetime.datetime.now() - relativedelta(days=1)
justdate = date.strftime("%x")
justtime = date.strftime("%X")

print(date)
print(justdate)
print(justtime)

date = datetime.datetime.now() - relativedelta(years=1)
justdate = date.strftime("%x")
justtime = date.strftime("%X")

print(date)
print(justdate)
print(justtime)

date = datetime.datetime.now()
justmonth = date.strftime("%B")
print(justmonth)

date = datetime.datetime.now() - relativedelta(months=1)
justmonth = date.strftime("%B")
print(justmonth)
