import pygame as pg
from pygame.locals import KEYDOWN, QUIT

# TODO: Put this on client side
class Patient(pg.sprite.Sprite):
    def __init__(self, color, width, height, xlim, ylim):
        super().__init__()

        self.image = pg.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()  # get rectangle corresponding to image, position can be updated via rect.x and rect.y
        self.xlim = xlim
        self.ylim = ylim

    # TODO: Send updated player status to the game object
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x = max(self.rect.x - 10, self.xlim[0])
        if keys[pg.K_RIGHT]:
            self.rect.x = min(self.rect.x + 10, self.xlim[1])
        if keys[pg.K_UP]:
            self.rect.y = max(self.rect.y - 10, self.ylim[0])
        if keys[pg.K_DOWN]:
            self.rect.y = min(self.rect.y + 10, self.ylim[1])

class Game:
    def __init__(self, display_width, display_height):
        self.dw = display_width
        self.dh = display_height
        self.patients = pg.sprite.Group()

    def add_patient(self, color, width, height, xlim, ylim, position):
        p = Patient(color, width, height, xlim, ylim)
        p.rect.x = position[0]
        p.rect.y = position[1]
        self.patients.add(p)
    
    def remove_patient(self, p):
        p.kill()
    
    def run(self):
        '''
        Implements the main game loop.
        '''
        pg.init()
        screen = pg.display.set_mode((self.dw, self.dh))
        running = True
        clock = pg.time.Clock()

        while running:

            event = pg.event.poll()
            if event.type == QUIT:
                running = False
            
            self.patients.update()  # update state of each patient
            screen.fill((0, 128, 0))
            self.patients.draw(screen)  # draw patients to surface (arbitrary order)
            pg.display.flip()  # update screen content
            clock.tick(60)


DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800
SPRITE_WIDTH = 30
SPRITE_HEIGHT = 30
XLIM = [0, DISPLAY_WIDTH-SPRITE_WIDTH]
YLIM = [0, DISPLAY_HEIGHT-SPRITE_HEIGHT]

game = Game(DISPLAY_WIDTH, DISPLAY_HEIGHT)
game.add_patient((255,255,0), 30, 30, XLIM, YLIM, [0, 0])
game.run()
