a = int("0x5852f", 16)
b = int("0x452f", 16)

print(hex(a-b))

a = ord("G")
print(a)

letters = [108, 105, 115, 116]

a = ""

for i in letters:
    a += chr(i)

print (a)


total = 0
for abc in range(5):
    total = total + abc
print(total)