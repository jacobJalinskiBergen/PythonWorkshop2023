import random

RANKS = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
SUITS = ("Clubs", "Spades", "Hearts", "Diamonds")

#Card Class for simulating playing cards
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return self.rank + " of " + self.suit

#Deck class for simulating deck of cards
class Deck:
    def __init__(self):
        self.__cards = []
        self.shuffle()
    
    def shuffle(self):
        self.__cards = []
        for rank in RANKS:
            for suit in SUITS:
                self.__cards.append(Card(rank, suit))
        
        #self.__cards = [Card(r, s) for r in RANKS for s in SUITS]
        random.shuffle(self.__cards)

    def draw(self):
        output = self.__cards[-1]
        del self.__cards[-1]
        return output
    
    def discard(self, card):
        a = random.randrange(0, len(self.__cards)+1)
        self.__cards.insert(a, card)

