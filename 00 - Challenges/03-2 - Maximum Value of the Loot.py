


def priceOf(it):
    it = it.split(" ")
    return int(it[0])

def amountOf(it):
    it = it.split(" ")
    return int(it[1])

def valueOf(it):
    return float(priceOf(it)/amountOf(it))



pricesAndAmounts = []
takenCompounds = []
compoundsAndCapacity = input()
compoundsAndCapacity = compoundsAndCapacity.split(" ")
howManyCompounds = int(compoundsAndCapacity[0])
capacityOfbackpack = int(compoundsAndCapacity[1])
totalValue = 0
whichComp = 0

for i in range(0, howManyCompounds):
    pricesAndAmounts.append(input())

sortedValues = sorted(pricesAndAmounts, key=lambda x: float(valueOf(x)))
sortedValues.reverse()



while True:
    if whichComp == len(sortedValues): break
    if amountOf(sortedValues[whichComp]) >= capacityOfbackpack:
        takenCompounds.append([whichComp, capacityOfbackpack])
        break
    else:
        takenCompounds.append([whichComp, amountOf(sortedValues[whichComp])])
        capacityOfbackpack -= amountOf(sortedValues[whichComp])
    whichComp += 1

for i in range (0,len(takenCompounds)):
    #print(takenCompounds[i][1])
    totalValue += takenCompounds[i][1] * valueOf(sortedValues[i])




print(totalValue)
    

