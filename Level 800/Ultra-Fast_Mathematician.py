a_bi = input()
b_bi = input()

print(bin(int(a_bi, 2) ^ int(b_bi, 2))[2:].zfill(len(a_bi)))
