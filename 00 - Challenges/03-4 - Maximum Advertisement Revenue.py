def strArraytoIntArray(arrStr):
    arrStr = arrStr.split(" ")
    returning = []
    for i in arrStr:
        returning.append(int(i))
    return returning

total = 0

howManySlots = input()
howManySlots = int(howManySlots)

arrStr1 = input()
arrInt1 = strArraytoIntArray(arrStr1)

arrStr2 = input()
arrInt2 = strArraytoIntArray(arrStr2)

arrInt1.sort()
arrInt2.sort()

arrInt1.reverse()
arrInt2.reverse()

for i in range(0, howManySlots):
    total += arrInt1[i] * arrInt2[i]

print(total)