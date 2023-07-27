def smallestMultiple(number):
    for i in range(1, 21):
        if number % i != 0:
            return False
    return True


i = 2520

while not smallestMultiple(i):
    i += 20


print(i)