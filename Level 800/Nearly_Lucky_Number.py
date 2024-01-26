inp = input()

no_lucky = 0
for ch in list(inp):
    if ch == '7' or ch == '4':
        no_lucky += 1
print("YES") if no_lucky == 7 or no_lucky == 4 else print("NO")
