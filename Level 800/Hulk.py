n = int(input())

res = ""
for i in range(n):
    res += "I hate " if i % 2 == 0 else "I love "
    res += "that " if i != n-1 else "it"
    
print(res)
