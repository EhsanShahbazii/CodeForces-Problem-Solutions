inp = input()
sort_inp = inp.split("+")
sort_inp.sort()
res = ""
for i in sort_inp:
    res += i + "+"
    
print(res.strip("+"))
