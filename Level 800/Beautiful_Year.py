inp = int(input())

for i in range(inp + 1, 10000):
    if len(set(list(str(i)))) == 4:
        print(i)
        break
