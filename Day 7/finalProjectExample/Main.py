import pygame
import Card
import Deck
import Hand
from TextGenerator import text

GAME_SIZE = (1200,800)
TEST_TEXT = False

class Game:
    def __init__(self):
        #Create game window
        self.window = pygame.display.set_mode(GAME_SIZE)
        pygame.display.set_caption("Card Game")

        #Define main variables
        self.run = True
        self.clock = pygame.time.Clock()
        self.turn = 0 # 0 = Player; 1 = Computer
        self.phase = 0 # 0 = Draw Phase; 1 = Discard Phase
        self.deck = Deck.Deck()
        self.deck.populate()
        self.discardPile = Deck.Deck()
        self.pHand = Hand.Hand(self.deck, self.discardPile)
        self.cHand = Hand.Hand(self.deck, self.discardPile)    
        self.tgen = text.TextGen()
        self.showOpponentHand = False
        self.score = [0, 0]
        #self.discardPile.discard(self.deck.draw())

    def update(self):
        while (self.run):
            #Sets max framerate (Not needed for card game but I included it anyways)
            self.clock.tick(120)

            events = pygame.event.get()
            for event in events:
                #When the exit button at the top right is pressed:
                if event.type == pygame.QUIT:
                    self.run = False

                #When the user left clicks:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.turn != 2:
                        if self.turn and self.phase: #CPU's discard phase
                            self.cHand.discard(self.cHand.computerDiscard())
                            self.turn = 0
                            self.phase = 0
                        elif self.turn and not self.phase: #CPU's draw phase
                            self.cHand.draw()
                            self.phase = 1
                        elif not self.turn and not self.phase: #User's draw phase
                            self.pHand.draw()
                            self.phase = 1
                    else:
                        self.deck.populate()
                        self.cHand.clearHand()
                        self.pHand.clearHand()
                        self.discardPile.clearDeck()
                        for i in range(8):
                            self.cHand.draw()
                            self.pHand.draw()
                        self.turn = 0
                        self.phase = 0
                        
            #Specific instructions for when player's discard phase. Done to avoid tracking mouse position + show off button presses
            if not self.turn and self.phase: #User's discard phase (The only complicated one)
                keys = pygame.key.get_pressed()
                chosen = -1
                i = 0
                for k in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                    if chosen == -1 and keys[k]:
                        chosen = i
                    i+=1

                if chosen != -1:
                    self.pHand.discard(self.pHand.nthCard(chosen))
                    self.turn = 1   
                    self.phase = 0

            if self.deck.isEmpty():
                self.deck.merge(self.discardPile)

            if self.phase == 0 and self.turn != 2 and (self.pHand.checkWin() or self.cHand.checkWin()):
                if self.pHand.checkWin():
                    self.score[0] += 1
                else:
                    self.score[1] += 1
                self.turn = 2

            self.draw()

    def draw(self):
        #The following if statement and its contents are for debugging purposes
        if TEST_TEXT:
            self.window.fill((128, 128, 196))
            self.tgen.makeText(self.window, 0, 0, "a quick brown fox. jumps over the lazy dog!".upper(), 2)
            self.tgen.makeText(self.window, 0, 24, "a quick brown fox, jumps over the lazy dog?", 2)
            self.tgen.makeText(self.window, 0, 48, "@-#$98765432_10 \\'\"{[(a lot)]}\"' /<5+2*1 = 7%>", 2)
            self.tgen.makeText(self.window, 0, 72, "`Me & Pizza ~ <3` ^^^\n", 2)

            pygame.draw.rect(self.window, (128, 110, 255), (GAME_SIZE[0]//2 - 20, GAME_SIZE[1]//2 - 20, 40, 40))
            midText = self.tgen.getCoordsFromCenter(GAME_SIZE[0]//2, GAME_SIZE[1]//2, "Middle Text - Gingerbread!!!", 3)
            self.tgen.makeText(self.window, midText[0], midText[1], "Middle Text - Gingerbread!!!", 3)

            pygame.display.update()
            return

        #Actual Draw Function
        #---------------------

        #Draw Board
        self.window.fill((171, 139, 99))
        pygame.draw.rect(self.window, (92, 49, 6), (0, 0, GAME_SIZE[0]+1, int(GAME_SIZE[1]/3)+1))
        pygame.draw.rect(self.window, (92, 49, 6), (0, int(2*GAME_SIZE[1]/3), GAME_SIZE[0]+1, int(GAME_SIZE[1]/3)+5))
        pygame.draw.line(self.window, (0, 0, 0), (0, int(GAME_SIZE[1]/3)+1), (GAME_SIZE[0], int(GAME_SIZE[1]/3)+1), 1+(GAME_SIZE[0] // 200))
        pygame.draw.line(self.window, (0, 0, 0), (0, int(2*GAME_SIZE[1]/3)), (GAME_SIZE[0], int(2*GAME_SIZE[1]/3)), 1+(GAME_SIZE[0] // 200))

        #Display Score
        scoreTxt = str(self.score[0]) + "-" + str(self.score[1])
        fontSize = int((GAME_SIZE[0]//3) / (10*len(scoreTxt)))
        fontSize = max(1, min(fontSize, int(GAME_SIZE[1]/36)))
        midText = self.tgen.getCoordsFromCenter(GAME_SIZE[0]//2, GAME_SIZE[1]//2, scoreTxt, fontSize)
        self.tgen.makeText(self.window, midText[0], midText[1], scoreTxt, fontSize)

        #Display draw deck
        deckHeight = min((2664*GAME_SIZE[0])//7020, 8*GAME_SIZE[1]//30)
        self.deck.display(self.window, GAME_SIZE[0]//30, GAME_SIZE[1]//3 + GAME_SIZE[1]//30, deckHeight, False)

        #Display discard pile
        self.discardPile.display(self.window, 2*GAME_SIZE[0]//3 + 9*GAME_SIZE[0]//30 - int(234*deckHeight/333), GAME_SIZE[1]//3 + GAME_SIZE[1]//30, deckHeight, True)

        #Draw CPU Cards
        self.cHand.display(self.window, 0, 0, GAME_SIZE[0], GAME_SIZE[1]//3, self.turn == 2)

        #Draw User Cards
        self.pHand.display(self.window, 0, 2*GAME_SIZE[1]//3, GAME_SIZE[0], GAME_SIZE[1]//3, True)

        #Update screen
        pygame.display.update()

def main():
    newGame = Game()
    newGame.update()
main()