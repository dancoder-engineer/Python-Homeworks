import DeckOfCards

deck = DeckOfCards.Deck()
#deck.seeDeck()
deck.test = 99

myHand = []
for i in range(0, 5):
    myHand.append(deck.dealCard())

for i in myHand:
    print(i)

deck.__init__()
