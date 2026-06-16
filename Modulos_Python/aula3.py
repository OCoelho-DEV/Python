# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

fmt = '%d/%m/%Y'
# date = datetime(2022, 12, 3, 7, 55, 10)
date = datetime.strptime('2022-12-3 07:55:10', '%Y-%m-%d %H:%M:%S')

print(date)
print(date.strftime(fmt))
print(date.strftime('%d/%m/%Y'))
print(date.strftime('%d/%m/%Y %H:%M'))
print(date.strftime('%d/%m/%Y %H:%M:%S'))
print(date.strftime('%Y'), date.year)
print(date.strftime('%H'), date.hour)
print(date.strftime('%M'), date.minute)
print(date.strftime('%S'), date.second)
