n = int(input())

no_room = 0
for i in range(n):
    p,q = list(map(int, input().split()))
    if q - p > 1 : no_room += 1
    
print(no_room)
