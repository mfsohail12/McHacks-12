import pygame as pg
from pygame.locals import KEYDOWN, QUIT
import time
from player import Patient, Staff

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

    def add_patient(self, name, sprite_path, n_frames, frame_rate, width, height, scale, pos, xlim, ylim):
        '''
        Add patient sprite to game.
        '''
        p = Patient(name, width, height, pos, xlim, ylim)
        p.rect.x = pos[0]
        p.rect.y = pos[1]
        p.init_sprite(sprite_path, n_frames, frame_rate, width, height, scale)
        self.patients.add(p)

    def add_staff(self, name, sprite_path, dialogue_path, width, height, pos):
        '''
        Add staff sprite to game.
        '''
        s = Staff(name, sprite_path, dialogue_path, width, height, pos)
        s.rect.x = pos[0]
        s.rect.y = pos[1]
        self.staff.add(s)
    
    def remove(self, name):
        '''
        Remove patient/staff from game.
        '''
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
            self.staff.update(self.patients)
            self.patients.draw(self.screen)  # draw patients to surface (arbitrary order)
            self.staff.draw(self.screen)

            pg.display.flip()  # update screen content
            clock.tick(60)


if __name__ == '__main__':
    DISPLAY_WIDTH  = 640
    DISPLAY_HEIGHT = 640

    PLAYER_WIDTH   = 16
    PLAYER_HEIGHT  = 16
    PLAYER_SCALE   = 4
    STAFF_WIDTH    = 40
    STAFF_HEIGHT   = 40
    SPRITE_RATE    = 20

    XLIM = [0, DISPLAY_WIDTH-PLAYER_WIDTH]
    YLIM = [0, DISPLAY_HEIGHT-PLAYER_HEIGHT]

    game = Game(DISPLAY_WIDTH, DISPLAY_HEIGHT)
    game.initialize()
    game.load_static_images()

    p0_spritesheet = '/Users/Ritchie/Desktop/U4 Winter/mchacks/McHacks-12/server/graphics/16PixelSlime/BlueSlime/BlueSlimeWalking-Sheet.png'
    n_frames = 4
    game.add_patient('John', p0_spritesheet, n_frames, SPRITE_RATE, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SCALE, [0,0], XLIM, YLIM)

    staff_path = '/Users/Ritchie/Desktop/U4 Winter/mchacks/McHacks-12/server/graphics/female_patient_generated_edited.png'
    dialogue_path = '/Users/Ritchie/Desktop/U4 Winter/mchacks/McHacks-12/server/dialogue/mary.txt'
    game.add_staff('Mary', staff_path, dialogue_path, STAFF_WIDTH, STAFF_HEIGHT, [450,50])

    game.run()