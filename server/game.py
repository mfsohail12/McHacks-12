import pygame as pg
from pygame.locals import KEYDOWN, QUIT
import time
from player import Patient, Staff
from constants import *
from Network import Network
import pickle
import json

class Game:
    def __init__(self, display_width, display_height):
        self.dw = display_width
        self.dh = display_height
        self.patient_names = set()
        self.patients = pg.sprite.Group()
        self.staff = pg.sprite.Group()

    def initialize(self):
        pg.init()
        self.screen = pg.display.set_mode((self.dw, self.dh))

    def load_static_images(self):
        self.bkg_img = pg.image.load('graphics/grass.png').convert_alpha()
        self.house1 = pg.image.load('graphics/House1.png').convert_alpha()

    def get_patient_data(self, name):
        '''
        Retrieve data corresponding to a patient.
        '''
        for p in self.patients:
            if p.name == name:
                return p.get_data()

    def add_patient(self, name, sprite_path, n_frames, frame_rate, width, height, scale, pos_x, pos_y, xlim, ylim, main_char=False):
        '''
        Add patient sprite to game.
        '''
        p = Patient(name, width, height, scale, pos_x, pos_y, xlim, ylim)
        p.rect.x = pos_x
        p.rect.y = pos_y
        p.init_sprite(sprite_path, n_frames, frame_rate)
        self.patients.add(p)
        self.patient_names.add(name)

        if main_char:
            self.main_char = p

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

        network = Network()
        # patient = network.getP()

        while running:

            event = pg.event.poll()
            if event.type == QUIT:
                running = False
            
            # main_char_data = json.dumps(self.main_char.get_data()).encode('utf-8')
            # print("Sending: ", main_char_data)
            other_patient_data = network.send(self.main_char.get_data())
            if not(other_patient_data is None) and not("EMPTY" in other_patient_data.keys()):
                for k, v in other_patient_data.items(): 
                    if not(k in self.patient_names):  # bring into patient group on first pass
                        self.add_patient(**v)
                    else:
                        for p in self.patients:
                            if p.name != self.main_char.name:
                                p.rect.x = v['pos_x']
                                p.rect.y = v['pos_y']

            # all_patients = [self.main_char] + [patient for patient in other_patients]
            # all_patients = [patient] + [Patient(data.name, data.width, data.height, data.pos, data.xlim, data.ylim) for data in other_patient_data]
            # self.patients.add(all_patients)

            self.screen.blit(self.bkg_img, (0,0))
            self.screen.blit(self.house1, (250,200))
            self.patients.update()  # update state of each patient

            # self.staff.update(self.patients)
            self.patients.draw(self.screen)  # draw patients to surface (arbitrary order)
            self.staff.draw(self.screen)

            pg.display.flip()  # update screen content
            clock.tick(60)


if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--name',  required=True, type=str, help='Name of character to add.')
    parser.add_argument('--color', required=True, type=str, help='Colour of character sprite.')
    args = parser.parse_args()

    # ---------------
    # Initialize game
    # ---------------
    game = Game(DISPLAY_WIDTH, DISPLAY_HEIGHT)
    game.initialize()
    game.load_static_images()

    # -----------------------------------
    # Initialize patient's main character
    # -----------------------------------
    p0_spritesheet = SPRITE_SHEETS[args.color]
    n_frames = 4
    game.add_patient(args.name, p0_spritesheet, n_frames, SPRITE_RATE, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SCALE, 0, 0, XLIM, YLIM, main_char=True)

    # p_data = game.get_

    staff_path = '/Users/Ritchie/Desktop/U4 Winter/mchacks/McHacks-12/server/graphics/female_patient_generated_edited.png'
    dialogue_path = '/Users/Ritchie/Desktop/U4 Winter/mchacks/McHacks-12/server/dialogue/mary.txt'
    game.add_staff('Mary', staff_path, dialogue_path, STAFF_WIDTH, STAFF_HEIGHT, [450,50])

    game.run()