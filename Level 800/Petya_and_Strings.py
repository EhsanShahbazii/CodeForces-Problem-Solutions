lex1 = input().lower()
lex2 = input().lower()

flag = False
for i in range(len(lex1)):
    if ord(lex1[i]) > ord(lex2[i]):
        print(1)
        flag = True
        break
    if ord(lex1[i]) < ord(lex2[i]):
        print(-1)
        flag = True
        break
    
if not flag:
    print(0)
