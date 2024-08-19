a,b = list(map(int, input().split()))

i = 0
while True:
    if a > b:
        print(i)
        break
    a *= 3
    b *= 2
    i += 1
