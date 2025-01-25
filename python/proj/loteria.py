from random import randint
num = []

while len(num) < 6:
    n = randint(1, 60)
    if n not in num:
        num.append(n)


print(sorted(num))
