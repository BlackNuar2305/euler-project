def simpleNumber(number):
    k = 2
    while k * k <= number:
        if number % k == 0:
            return False
        k += 1
    return True

i = 2
count = 0
while count < 10001:
    if simpleNumber(i):
        count += 1
    i += 1
print(i-1)