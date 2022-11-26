import DeckOfCards

deck = DeckOfCards.Deck()
playerHand = []
dealerHand = []
playerMoney = 500
keepPlaying = True

def dealerPlay():
  dealerValue = 0
  while dealerValue < 17:
    dealerHand.append(deck.dealCard())
    dealerValue = handValue(dealerHand)

  showHand(dealerHand)
  print()
  print("Hand Value: " + str(handValue(dealerHand)))

  if handValue(dealerHand) > 21:
    print("Dealer is over!")
    return 0
  else:
    return handValue(dealerHand)

def handValue(hand):
  totalValue = 0
  noOfAces = 0
  index = 0

  while index < len(hand):
    totalValue += hand[index].value
    if hand[index].rank == "Ace":
        noOfAces += 1
    index += 1

  i = 0

  if totalValue > 21 and noOfAces > 0:
    while i < noOfAces:
        totalValue -= 10
        i += 1
        if totalValue < 21:
            break

  return totalValue

def showHand(hand):
  for i in hand:
    print(i)

def dealersCard():
  print("Dealer is showing the " + str(dealerHand[1]))


def checkMoney():
  if playerMoney <= 0:
    print("You are now broke, and will starve to death beginning immediately.")
    print("Sorry, you will not starve to death THAT soon, because you're")
    print("staying at the Tropicana Hotel & Casino, where you have access to")
    print("all you can drink orange juice for the entire length of your stay.")
    print("You're paid through next week, so you'll begin starving to death")
    print("then. Game over!")
    keepPlaying = False
    return 0
  elif playerMoney > 5000:
    print("You have bankrupted the casino! What kind of casino is so poorly")
    print("run that the house loses enough to the point of bankruptcy? Only")
    print("one run by Donald Trump could be so incompetent. If only he had")
    print("colluded with Russia on how to run a casino...")
    keepPlaying = False
    return 0
  else:
    return 0

def playerPlay():
  hitMore = True
  playerHand.append(deck.dealCard())

  while hitMore:
    playerHand.append(deck.dealCard())
    print("In your hand, you have:")
    showHand(playerHand)
    print("The total value of these is " + str(handValue(playerHand)))

    if handValue(playerHand) > 21:
      print ("Player is over!")
      print()
      return 0

    likeHit = ""
    while True:
      likeHit = input ("Would you like to hit (Y/N)? ")
      if likeHit == "N":
        hitMore = False
        return handValue(playerHand)
      elif likeHit == "Y":
        break


        

if __name__ == "__main__":
  dealerScore = 0
  playerScore = playerPlay()
  if playerScore <= 21:
    dealerScore = dealerPlay()

