a = int(input())
sum = 0
c = []
s = 0
while True:
    sum += a
    c += [a]
    a = int(input())
    if sum == 0:
        for i in c:
            s += i * i
        print(s)
        break
        