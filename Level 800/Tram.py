n = int(input())

cap = current = 0
for i in range(n):
    a,b = list(map(int, input().split()))
    current += b - a
    cap = current if current > cap else cap
    
print(cap)
