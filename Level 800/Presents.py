n = int(input())
inp = list(map(int, input().split()))

res = ""
for i in range(1, n+1):
    res += f"{inp.index(i) + 1} "
    
print(res)
