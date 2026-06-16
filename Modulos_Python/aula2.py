# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
starter_date = datetime.strptime('10/03/2025 09:30:00', fmt)
final_date = datetime.strptime('20/04/2026 09:30:01', fmt)
# delta = timedelta(days=10, hours=2)
delta = relativedelta(final_date, starter_date)
print(delta.days, delta.years)

# print(final_date + delta)
# print(final_date + relativedelta(seconds=59, minutes=10))