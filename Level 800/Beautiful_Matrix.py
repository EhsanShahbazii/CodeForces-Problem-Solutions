for i in range(5):
    inp = input()
    if '1' in inp:
        print(abs(inp.split(' ').index('1') - 2) + abs(i - 2))
