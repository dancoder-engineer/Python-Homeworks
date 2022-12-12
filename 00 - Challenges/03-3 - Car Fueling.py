distanceBetweenCities = 0
howFarOnFullTank = 0
howManyGasStations = 0
gasStationDistancesString = ""
gasStationDistances = [0]
gasInTank = -1
howManyFillUps = 0

def setToConstants():
    global distanceBetweenCities
    global howFarOnFullTank
    global howManyGasStations
    global gasStationDistancesString

    distanceBetweenCities = 950
    howFarOnFullTank = 400
    howManyGasStations = 4
    gasStationDistancesString = "200 375 550 750"

def userInput():
    global distanceBetweenCities
    global howFarOnFullTank
    global howManyGasStations
    global gasStationDistancesString
    global gasStationDistances

    distanceBetweenCities = input()

    if distanceBetweenCities == "-999":
        setToConstants()
        return 0

    howFarOnFullTank = input()
    howManyGasStations = input()
    gasStationDistancesString = input()

    distanceBetweenCities = int(distanceBetweenCities)
    howFarOnFullTank = int(howFarOnFullTank)
    howManyGasStations = int(howManyGasStations)

def fillUp():
    global gasInTank
    global howManyFillUps
    gasInTank = howFarOnFullTank
    howManyFillUps += 1




def main():
    global gasStationDistancesString
    global gasStationDistances
    global gasInTank
    global howManyFillUps

    gasInTank = howFarOnFullTank

    userInput()
    gasStationDistancesString = gasStationDistancesString.split(" ")
    
    for i in gasStationDistancesString:
        gasStationDistances.append(int(i))

    gasStationDistances.append(distanceBetweenCities)

   # print(gasStationDistances)

    for i in range(0, howManyGasStations+1): 
        if i == 0: gasInTank = howFarOnFullTank
        try:
            nextDistance = gasStationDistances[i+1] - gasStationDistances[i]
     #       print(str(gasStationDistances[i+1]) + " " + str(gasStationDistances[i]) )
        except:
            pass
        
    #    if i == 0: nextDistance = gasStationDistances[0]
    #    print("We're at stop " + str(i) + " and our gas is at " + str(gasInTank) + ". There are " + str(howManyGasStations) + " stops. The next gas station's distance is " + str(nextDistance))

           # nextDistance = gasStationDistances[i]

      #  print(str(nextDistance) + " " + str(gasInTank))
        if nextDistance < 1: nextDistance = 0
        if nextDistance > howFarOnFullTank:
            print(-1)
            return 0
        elif nextDistance > gasInTank:
#            if howManyGasStations == i: continue
      #      print("Fill at " + str(i) + " because the next distance is " + str(nextDistance) + " away and we have " + str(gasInTank) )
            fillUp()
            gasInTank -= nextDistance
        else:
            gasInTank -= nextDistance
            
    print(howManyFillUps)






if __name__ == "__main__":
    main()