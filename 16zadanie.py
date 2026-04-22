a = int(input())
while a != 0:
    if a % 6 == 0 and a % 10 == 4:
            a += a
    if a == 0:
        print(a)
        break