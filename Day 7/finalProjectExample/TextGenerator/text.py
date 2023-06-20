import pygame

class TextGen:
    def __getImg(self, i):
        try:
            return pygame.image.load("TextGenerator/Font/" + str(i) + ".png")
        except:
            return self.__unknownImg
            
    def __init__(self):
        self.__unknownImg = pygame.image.load("TextGenerator/Font/128.png")
        self.__imgs = {i: self.__getImg(i) for i in range(256)}
    
    def makeText(self, window, x, y, string, fontSize = 1):
        chars = [ord(c) for c in string]
        canvas = pygame.Surface((len(chars)*10*fontSize, 12*fontSize))
        canvas.set_colorkey((255, 255, 255))
        canvas.fill((255, 255, 255))
        for i, char in enumerate(chars):
            img = self.__imgs[char]
            img = pygame.transform.scale(img, (10*fontSize, 12*fontSize))
            canvas.blit(img, (i*10*fontSize, 0))
        window.blit(canvas, (x, y))

    def getCoordsFromCenter(self, x, y, string, fontSize = 1):
        dim = (len(string)*10*fontSize, 12*fontSize)
        return [int(x - dim[0]//2), int(y - dim[1]//2)]