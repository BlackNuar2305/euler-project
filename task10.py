def simpleNumber(number):
    k = 2
    while k**2 <= number:
        if number % k == 0:
            return False
        k += 1
    return True


i = 1999999
summa = 2

while i > 1:
    if simpleNumber(i):
        summa += i

    i -= 2


print(summa)