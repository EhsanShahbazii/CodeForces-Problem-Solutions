n, k = list(map(int, input().split()))

for i in range(k):
    n = n / 10 if n % 10 == 0 else n - 1
print(int(n))
