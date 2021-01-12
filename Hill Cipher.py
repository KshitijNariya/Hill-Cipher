a = [[0] * 2 for v in range(2)]
b = [[0] for r in range(2)]
c = [[0] for t in range(2)]

key = input("Enter Your Key: ")
k=0
for i in range(2):
    for j in range(2):
        a[i][j] = ord(key[k]) % 65
        k+=1

pt = input("Enter Plain Text: ")
for i in range(2):
    b[i][0] = ord(pt[i]) % 65


for i in range(2):
    for j in range(1):
        c[i][j] = 0
        for x in range(2):
            c[i][j] += (a[i][x] * b[x][j])
        c[i][j] = c[i][j] % 26

enc = []
for i in range(2):
    enc.append(chr(c[i][0] + 65))

print("Ciphertext: ", "".join(enc))