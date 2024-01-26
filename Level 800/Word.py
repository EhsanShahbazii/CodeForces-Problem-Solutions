inp = input()

no_lower_ch = 0
lower_inp = inp.lower()
for i in range(len(inp)):
    if inp[i] == lower_inp[i]:
        no_lower_ch += 1
        
print(inp.lower()) if no_lower_ch >= len(inp)/2 else print(inp.upper())
