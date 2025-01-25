import pygame as pg
from pygame.locals import KEYDOWN, QUIT
import time

# TODO: Put this on client side
class Patient(pg.sprite.Sprite):
    def __init__(self, name, sprite_path, pos, xlim, ylim, width, height):
        super().__init__() 
        self.name = name
        self.rect = pg.Rect(pos[0], pos[1], width, height)
        self.image = pg.image.load(sprite_path).convert_alpha()
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

class Staff(pg.sprite.Sprite):
    def __init__(self, name, sprite_path, pos, width, height):
        super().__init__()
        self.name = name
        self.rect = pg.Rect(pos[0], pos[1], width, height)
        self.image = pg.image.load(sprite_path).convert_alpha()

class Game:
    def __init__(self, display_width, display_height):
        self.dw = display_width
        self.dh = display_height
        self.patients = pg.sprite.Group()
        self.staff = pg.sprite.Group()

    def initialize(self):
        pg.init()
        self.screen = pg.display.set_mode((self.dw, self.dh))

    def load_static_images(self):
        self.bkg_img = pg.image.load('graphics/grass.png').convert_alpha()

    def add_patient(self, name, sprite_path, pos, xlim, ylim, width, height):
        p = Patient(name, sprite_path, pos, xlim, ylim, width, height)
        p.rect.x = pos[0]
        p.rect.y = pos[1]
        self.patients.add(p)

    def add_staff(self, name, sprite_path, pos, width, height):
        s = Staff(name, sprite_path, pos, width, height)
        s.rect.x = pos[0]
        s.rect.y = pos[1]
        self.staff.add(s)
    
    def remove(self, name):
        for sprite in self.staff:
            if sprite.name == name:
                sprite.kill()
        for sprite in self.patients:
            if sprite.name == name:
                sprite.kill()
    
    def run(self):
        '''
        Implements the main game loop.
        '''
        running = True
        clock = pg.time.Clock()

        while running:

            event = pg.event.poll()
            if event.type == QUIT:
                running = False
            
            self.screen.blit(self.bkg_img, (0,0))
            self.patients.update()  # update state of each patient
            self.patients.draw(self.screen)  # draw patients to surface (arbitrary order)
            self.staff.draw(self.screen)

            pg.display.flip()  # update screen content
            clock.tick(60)


DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 640
SPRITE_WIDTH = 30
SPRITE_HEIGHT = 30
XLIM = [0, DISPLAY_WIDTH-SPRITE_WIDTH]
YLIM = [0, DISPLAY_HEIGHT-SPRITE_HEIGHT]

game = Game(DISPLAY_WIDTH, DISPLAY_HEIGHT)
game.initialize()
game.load_static_images()

patient_path = '/Users/Ritchie/Desktop/U4 Winter/mchacks/McHacks-12/server/graphics/female_patient_generated_edited.png'
staff_path = '/Users/Ritchie/Desktop/U4 Winter/mchacks/McHacks-12/server/graphics/female_patient_generated_edited.png'
game.add_patient('John', patient_path, [0,0], XLIM, YLIM, 30, 30)
game.add_staff('Mary', staff_path, [450,50], 30, 30)
game.run()