import Deck

RANKS = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King")
SUITS = ("Clubs", "Spades", "Hearts", "Diamonds")

def main():
    misses = 0
    for s in SUITS:
        for r in RANKS:
            c = Deck.Card(r, s)
            yourResponse = str(c)
            myResponse = r + " of " + s
            if yourResponse == myResponse:
                a = "  Correct"
            else:
                a = "Incorrect"
                misses += 1
            print(a, "Your response - \"" + yourResponse + '"', "Required answer - \"" + myResponse + '"', sep = " : ")
    print("Total wrong:", misses)
main()