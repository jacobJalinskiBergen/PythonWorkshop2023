import pygame
GAME_SIZE = (1600, 900)

class Game:
    def __init__(self):
        #Create game window
        pygame.init()
        self.window = pygame.display.set_mode(GAME_SIZE)
        pygame.display.set_caption("Windows LockScreen")
        self.font = pygame.font.SysFont("monospace", 200) #(font style, font size)

        self.clock = pygame.time.Clock()
        self.run = True

        pygame.mouse.set_visible(False)

        self.rect = {"x":(GAME_SIZE[0]//3), "y":(GAME_SIZE[1]//3), "velocity":[18, 25]}
        self.circle = {"x":((3*GAME_SIZE[0])//4), "y":(GAME_SIZE[1]//3), "velocity":[-30, 24]}
        self.frend = {"x":((GAME_SIZE[0])//4), "y":(GAME_SIZE[1]//2), "velocity":[8, -12], "image":pygame.image.load("frend.png")}
        self.frend["image"] = pygame.transform.scale(self.frend["image"], (64, 64))
        self.me = {"x":(GAME_SIZE[0]//2), "y":(GAME_SIZE[1]//2), "velocity":[0, 32]}
        self.mateo = {"x":((3*GAME_SIZE[0])//4), "y":((3*GAME_SIZE[1])//4), "velocity":[10, -5], "shape":0}

        while self.run:
            self.update()
            self.draw()

    def update(self):
        self.clock.tick(30)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mateo["velocity"] = [-1 * i for i in self.mateo["velocity"]]
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.me["velocity"] = [-32, 0]
        if keys[pygame.K_RIGHT]:
            self.me["velocity"] = [32, 0]
        if keys[pygame.K_UP]:
            self.me["velocity"] = [0, -32]
        if keys[pygame.K_DOWN]:
            self.me["velocity"] = [0, 32]
        

        for shape in [self.rect, self.circle, self.frend, self.me, self.mateo]:
            shape["x"] += shape["velocity"][0]
            shape["y"] += shape["velocity"][1]

            bounced = False

            if shape["y"] > GAME_SIZE[1]:
                shape["y"] = 2*GAME_SIZE[1] - shape["y"]
                shape["velocity"][1] *= -1
                bounced = True
            if shape["x"] > GAME_SIZE[0]:
                shape["x"] = 2*GAME_SIZE[0] - shape["x"]
                shape["velocity"][0] *= -1
                bounced = True
            if shape["x"] < 0:
                shape["x"] *= -1
                shape["velocity"][0] *= -1 
                bounced = True
            if shape["y"] < 0:
                shape["y"] *= -1
                shape["velocity"][1] *= -1
                bounced = True
            
            if bounced and "shape" in shape:
                shape["shape"] -= 1
                shape["shape"] *= -1



    def draw(self):
        self.window.fill((64, 0, 80))

        text = self.font.render("Hello World!", False, (255, 150, 150))
        self.window.blit(text, (0, 0))

        pygame.draw.rect(self.window, (160, 160, 255), (self.rect["x"] - 20, self.rect["y"] - 20, 40, 40))
        pygame.draw.circle(self.window, (255, 80, 110), (self.circle["x"], self.circle["y"]), 30)
        self.window.blit(self.frend["image"], (self.frend["x"] - 32, self.frend["y"] - 32))
        pygame.draw.circle(self.window, (0, 160, 20), (self.me["x"], self.me["y"]), 40)
        if self.mateo["shape"] == 1:
            pygame.draw.circle(self.window, (0, 0, 0), (self.mateo["x"], self.mateo["y"]), 30)
        else:
            pygame.draw.rect(self.window, (0, 0, 0), (self.mateo["x"]-30, self.mateo["y"]-30, 60, 60))

        mousePos = pygame.mouse.get_pos()
        pygame.draw.circle(self.window, (190, 80, 255), (mousePos[0], mousePos[1]), 10)

        pygame.display.update()

Game()