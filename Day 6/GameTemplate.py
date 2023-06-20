import Deck

#Given the user's hand, it asks the user which card to discard and returns it
def userDiscardChoice(userHand):
    userResponse = ""
    strHand = [str(card).lower().strip() for card in userHand]
    run = True
    while run:
        userResponse = input("Which card you you want to discard?: ").lower().strip()
        if userResponse not in strHand:
            print("Invalid Card!")
        else:
            run = False
    return userHand[strHand.index(userResponse)]



#Given the AI's hand, return the card the AI wishes to discard
def aiDiscardChoice(compHand):
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


#Checks if a given hand has 4 cards of the same rank
#Returns true if a hand has 4 cards of the same rank
def checkFor4(hand):
    cardQuantity = {}
    for card in hand:
        if card.rank not in cardQuantity:
            cardQuantity[card.rank] = 1
        else:
            cardQuantity[card.rank] += 1
    for rank in cardQuantity:
        if cardQuantity[rank] >= 4:
            return True
    return False

#Return a string representing the hand as a comma seperated list
def handToString(hand):
    return ", ".join([str(card) for card in hand])

def main():
    #Define the hands of both the AI and the User as empty lists and the deck as a new deck object

    #Populate both the user hand and the AI hand with a for loop. Remember, both players start with 8 cards!
    
    #loop the game until one player has 4 of the same rank (aka. loop while both the user and the AI do not have 4 cards of the same rank)

        #Draw a card for the user

        #Tell the user that a card has been drawn

        #Reshow the user their deck

        #Ask the user for the card to discard. Collect it into a new variable

        #Remove the card from the user's hand

        #Add the card back into the deck at a random spot (not just the bottom of the deck. doing so could )

        #Check if user didn't yet win
            #Draw a card for the ai and tell the user that a card was drawn

            #discard a card for the ai and tell the user that a card was discarded
        
    #At this point in the code, one player must've won. First check the user, then check the ai. This is so that in the rare cases of ties, the user wins! (Computers don't get upset when odds are stacked against them)

    #Show both player's hands. This should be the one and only time the user sees the ai's hand

    #Check if the user won
        #If so, say the user won!
    #otherwise
        #user loses!

    #End of main function => end of game

main()
