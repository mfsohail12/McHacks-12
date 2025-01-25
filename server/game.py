import pygame as pg
from pygame.locals import KEYDOWN, QUIT

class Patient(pg.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pg.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()  # get rectangle corresponding to image, position can be updated via rect.x and rect.y

    def move_right(self, dist):
        self.rect.x += dist
    
    def move_left(self, dist):
        self.rect.x -= dist

    def move_forward(self, dist):
        self.rect.y += dist

    def move_backward(self, dist):
        self.rect.y -= dist


class Game:
    def __init__(self, display_width, display_height):
        self.dw = display_width
        self.dh = display_height
        self.patients = pg.sprite.Group()

    def add_patient(self, color, width, height, position):
        p = Patient(color, width, height)
        p.rect.x = position[0]
        p.rect.y = position[1]
        self.patients.add(p)
    
    def remove_patient(self, p):
        p.kill()
    
    def run(self):
        pg.init()
        screen = pg.display.set_mode((self.dw, self.dh))
        running = True
        clock = pg.time.Clock()

        while running:
            event = pg.event.poll()
            if event.type == QUIT:
                running = False
            
            keys = pg.key.get_pressed()
            if keys[pg.K_LEFT]:
                p0.move_left(10)
            if keys[pg.K_RIGHT]:
                p0.move_right(10)
            if keys[pg.K_DOWN]:
                p0.move_forward(10)
            if keys[pg.K_UP]:
                p0.move_backward(10)

            p0.update()
            screen.fill((0, 128, 0))
            all_patients.draw(screen)
            pg.display.flip()
            clock.tick(60)



DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800

game = Game(DISPLAY_WIDTH, DISPLAY_HEIGHT)



