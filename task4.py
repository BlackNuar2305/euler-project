def palindrom(number):
    string = str(number)
    for i in range(0, len(string) // 2):
        if string[i] != string[-(i+1)]:
            return False
    return True

maxPalindrom = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        if palindrom(i*j) and i * j > maxPalindrom:
            maxPalindrom = i * j


print(maxPalindrom)