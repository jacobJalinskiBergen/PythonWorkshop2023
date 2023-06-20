import Deck
import Card
import pygame

class Hand:
    #Defines a hand with 8 cards
    def __init__(self, drawDeck, discardDeck):
        self.__draw = drawDeck
        self.__discard = discardDeck
        self.__hand = [drawDeck.draw() for i in range(8)]
        self.sort()
    
    #If a card is in the person's hand, return it to the discard pile
    def discard(self, card):
        if card in self.__hand:
            self.__hand.remove(card)
            self.__discard.discard(card)

    #Draws a card from the deck
    def draw(self):
        self.__hand.append(self.__draw.draw())
        self.sort()

    #Sort by rank & suit
    #Uses tools beyond the scope of the mini-course so don't worry about it!
    def sort(self):
        self.__hand.sort(key=lambda x:x.sortingValue())

    #Displays the hand onto the screen
    def display(self, window, x, y, width, height, show = True):

        #Compute the positions of cards
        length = len(self.__hand)
        cardSeperation = int(width / (3 * length+1))
        cardHeight = min(int(height/4*3), int(cardSeperation*2/234*333))
        
        #Display Cards
        for i, c in enumerate(self.__hand): #Same as "for c in self.__hand:" with "i = self.__hand.index(c)"
            c.display(window, x+(3*i+1)*cardSeperation, int(y+height/8), cardHeight, show)
    
    #checks for a win in this hand
    def checkWin(self):
        cardQuantity = {}
        for card in self.__hand:
            if card.rank not in cardQuantity:
                cardQuantity[card.rank] = 1
            else:
                cardQuantity[card.rank] += 1
        for rank in cardQuantity:
            if cardQuantity[rank] >= 4:
                return True
        return False
    
    #Chooses a card to discard for the Computer Player
    def computerDiscard(self):
        compHand = self.__hand #This Line of code is here so I can copy + paste code from workshop 3
        cardQuantity = {}
        for card in compHand:
            if card.rank not in cardQuantity:
                cardQuantity[card.rank] = [1, card]
            else:
                cardQuantity[card.rank][0] += 1
        smallestQuantity = compHand[0].rank
        for rank in cardQuantity:
            if cardQuantity[smallestQuantity][0] > cardQuantity[rank][0]:
                smallestQuantity = rank
        return cardQuantity[smallestQuantity][1]
    
    #Returns the nth card in the hand. Returns error card if not in hand
    def nthCard(self, n):
        if n in range(len(self.__hand)):
            return self.__hand[n]
        return Card.Card("OOP", "OOP")
    
    def clearHand(self):
        for i in range(len(self.__hand)):
            self.discard(self.nthCard(0))