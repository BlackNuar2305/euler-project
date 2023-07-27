summa = 0
p = 1

for i in range(1, 101):
    summa += i**2
    p += i

print(p**2 - summa)