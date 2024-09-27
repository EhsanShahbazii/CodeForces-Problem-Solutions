n = input()
inp = input()

no_a = no_d = 0
for ch in list(inp):
    if ch == 'A':
        no_a += 1
    else:
        no_d += 1

if no_a > no_d:
    print("Anton")
elif no_a == no_d:
    print("Friendship")
else:
    print("Danik")
