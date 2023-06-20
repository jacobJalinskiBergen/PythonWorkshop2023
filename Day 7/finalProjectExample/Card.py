import pygame

RANKS = ("ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king")
SUITS = ("hearts", "diamonds", "spades", "clubs")

class Card:
    #Constructor
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.front = pygame.image.load("CardImages/" + suit + "_" + rank + ".png") if rank in RANKS and suit in SUITS else pygame.image.load("CardImages/blank_card.png")
        self.back = pygame.image.load("CardImages/back.png")
    
    #Draw card to window
    def display(self, window, x, y, height, front = True):
        width = int(height/333 * 234)
        toScale = self.front if front else self.back
        toBlit = pygame.transform.scale(toScale, (width, height))
        window.blit(toBlit, (x, y))

    #This converts the card to a value for sorting reasons
    def sortingValue(self):
        if self.rank in RANKS and self.suit in SUITS:
            return RANKS.index(self.rank) * 4 + SUITS.index(self.suit)
        return -1