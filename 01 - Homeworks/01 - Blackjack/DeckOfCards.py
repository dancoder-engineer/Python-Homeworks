import random

class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        if rank == "Jack" or rank == "Queen" or rank == "King":
            self.value = 10
        elif rank == "Ace":
            self.value = 11
        else:
            self.value = int(rank)

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():

    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suits = ["Clubs", "Spades", "Diamonds", "Hearts"]
        self.test = 9
        self.cards = []
        for i in ranks:
            for j in suits:
                card = Card(j, i)
                self.cards.append(card)
        random.shuffle(self.cards)

    def __len__(self):
        return len(self.cards)

    def seeDeck(self):
        for i in self.cards:
            print(i)

    def dealCard(self):
        return self.cards.pop(0)
