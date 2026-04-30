from itertools import count

c1 = count()

for i in c1:
    if i > 100:
        break
    print(i)