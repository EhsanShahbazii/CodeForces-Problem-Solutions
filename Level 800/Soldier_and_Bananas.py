k, n, w = list(map(int, input().split()))

borrow = int(k * (w * (w + 1) / 2) - n)
print(0) if borrow < 0 else print(borrow)
