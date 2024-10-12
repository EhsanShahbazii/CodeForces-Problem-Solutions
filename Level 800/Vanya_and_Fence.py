import math

n, h = list(map(int, input().split()))
arr = list(map(int, input().split()))

sum = 0
for i in arr:
    sum += math.ceil(i / h)
    
print(sum)
