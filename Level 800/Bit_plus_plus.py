no_of_lines = int(input())

result = 0
for i in range(no_of_lines):
    result += 1 if '+' in input() else result - 1

print(result)
