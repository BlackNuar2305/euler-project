from math import sqrt

num = 600851475143

def simpleNumber(number):
    k = 2
    while k * k < number:
        if number % k == 0:
            return False
        k += 1
    return True

n = 0

for i in range(3, int(sqrt(num))):
    if num % i == 0:
        if simpleNumber(i):
            n = i


print(n)
print(simpleNumber(n))