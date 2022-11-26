import DeckOfCards

deck = DeckOfCards.Deck()
myHand = []


def dealMyHand(): 
  for i in range(0, 2):
    myHand.append(deck.dealCard())

def myHandValue():
  totalValue = 0
  acePlaces = []
  index = 0

  while index < len(myHand):
    totalValue += myHand[index].value
    if myHand[index].rank == "Ace":
        acePlaces.append(index)
    index += 1

  i = 0

  if totalValue > 21 and len(acePlaces) > 0:
    while i < len(acePlaces):
        totalValue -= 10
        i += 1
        if totalValue < 21:
            break

 
    



  return totalValue

def showMyHand():
  for i in myHand:
    print(i)

def main():
  dealMyHand()
  showMyHand()
  print()
  print(myHandValue())

main()