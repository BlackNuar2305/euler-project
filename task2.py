a = 0
b = 1
s = []

while a < 4000000 or b < 4000000:
    if a > b:
        b = b + a
    else:
        a += b
    if a % 2 == 0 and a not in s:
        s.append(a)
    if b % 2 == 0 and b not in s:
        s.append(b)
    


print(sum(s))