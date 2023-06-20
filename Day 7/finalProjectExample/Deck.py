import pygame
import random
import Card

class Deck:
    #Creates an empty deck
    def __init__(self):
        self.__cards = []
    
    #True if the deck is empty. False if not
    def isEmpty(self):
        return len(self.__cards) == 0

    #Populates the deck of cards with all 52 cards and shuffles
    def populate(self):
        self.clearDeck()
        for r in Card.RANKS:
            for s in Card.SUITS:
                self.__cards.append(Card.Card(r, s))
        self.shuffle()
    
    #shuffles deck
    def shuffle(self):
        random.shuffle(self.__cards)

    #displays deck
    def display(self, window, x, y, height, show = True):
        if not self.isEmpty():
            self.__cards[-1].display(window, x, y, height, show)

    #Draws top card off deck
    def draw(self):
        if self.isEmpty():
            return Card.Card("OOP", "OOP")
        return self.__cards.pop()

    #Adds a card to the top of the deck
    def discard(self, card):
        self.__cards.append(card)

    #Removes cards from one deck and adds them to another. Shuffles deck
    def merge(self, deck):
        while not deck.isEmpty():
            self.discard(deck.draw())
        self.shuffle()

    #Clears Deck
    def clearDeck(self):
        self.__cards = []