import Deck

def resizeStr(st, sz = 20):
    return st + " " * (sz - len(st))

def main():
    d1 = Deck.Deck()
    d2 = Deck.Deck()
    print(resizeStr("Deck 1:"), "Deck 2:")
    print("-" * 40)
    for i in range(52):
        print(resizeStr(str(d1.draw())), d2.draw())

main()