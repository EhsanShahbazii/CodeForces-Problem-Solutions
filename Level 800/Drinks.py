n = int(input())
per = list(map(int, input().split()))

sum = 0
for p in per:
    sum += p/100
    
print(sum/n * 100)
