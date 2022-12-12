
totalAmt = input()
totalAmt = int(totalAmt)
#totalAmt = 8
place=0
coinCount = 0
denominations=[10, 5 ,1]
howManyOfEach = []

for i in range(0, len(denominations)+2):
    howManyOfEach.append(-1)




if __name__ == "__main__":
    for i in denominations:
        howManyOfThisCoin = int(totalAmt/i)
        coinCount += howManyOfThisCoin
        howManyOfEach[place] = howManyOfThisCoin
        totalAmt -= i*howManyOfThisCoin
        place += 1

print(coinCount)