sum = 0
a = int(input())
while a != 0:
    a = int(input())
    if a == 0:
        break
    if a > 9 and a < 100 and a % 8 == 0:
        sum += a
print(sum)