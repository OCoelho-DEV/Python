# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar

# print(calendar.calendar(2022))
# print(calendar.month(2026, 12))

# print(calendar.monthrange(2026, 3))
# print(list(enumerate(calendar.day_name)))

# first_day_number, last_day = calendar.monthrange(2026, 12)
# print(calendar.day_name[first_day_number])

# print(calendar.day_name[calendar.weekday(2022, 12, last_day)])

for week in calendar.monthcalendar(2022, 12):
    # print(tuple(enumerate(week)))
    # ((0, 0), (1, 0), (2, 0), (3, 1), (4, 2), (5, 3), (6, 4))
    # ((0, 5), (1, 6), (2, 7), (3, 8), (4, 9), (5, 10), (6, 11))
    # ((0, 12), (1, 13), (2, 14), (3, 15), (4, 16), (5, 17), (6, 18))
    # ((0, 19), (1, 20), (2, 21), (3, 22), (4, 23), (5, 24), (6, 25))
    # ((0, 26), (1, 27), (2, 28), (3, 29), (4, 30), (5, 31), (6, 0))
    for day in week:
        if day == 0:
            continue
        print(day)