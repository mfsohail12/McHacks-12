import pygame as pg

class SpriteSheet:
    def __init__(self, filename):
        self.sheet = pg.image.load(filename)
    
    def get_image(self, frame, width, height, scale):
        '''
        Args:
            frame  : Which frame of the slime spritesheet
            width  : Width of each frame
            height : Height of each frame
            scale  : Scale factor
        '''
        image = pg.Surface((width, height), pg.SRCALPHA)
        image.blit(self.sheet, (0, 0), (frame*width, 0, width, height))  # hook sheet onto point (0,0) and draw subsection over the area (x,y,w,h)
        image = pg.transform.scale(image, (width*scale, height*scale))
        return image

# TODO: Put this on client side
class Patient(pg.sprite.Sprite):
    def __init__(self, name, width, height, scale, pos_x, pos_y, xlim, ylim):
        super().__init__() 
        self.name        = name
        self.width       = width
        self.height      = height
        self.scale       = scale
        self.rect        = pg.Rect(pos_x, pos_y, width, height)
        self.xlim        = xlim
        self.ylim        = ylim
        self.frame_count = 0

    def init_sprite(self, sprite_path, n_frames, frame_rate):
        self.sprite_path = sprite_path
        self.spritesheet = SpriteSheet(sprite_path)
        self.n_frames    = n_frames
        self.frame_rate  = frame_rate
        self.frames      = [self.spritesheet.get_image(f, self.width, self.height, self.scale) for f in range(n_frames)]
    
    def get_data(self):
        return {'name':        self.name,
                'width':       self.width,
                'height':      self.height,
                'scale':       self.scale,
                'pos_x':       self.rect.x,
                'pos_y':       self.rect.y,
                # 'pos':         [self.rect.x, self.rect.y],
                'xlim':        self.xlim,
                'ylim':        self.ylim,
                'sprite_path': self.sprite_path,
                'n_frames':    self.n_frames,
                'frame_rate':  self.frame_rate}

    def update_input(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.x = max(self.rect.x - 5, self.xlim[0])
        if keys[pg.K_RIGHT]:
            self.rect.x = min(self.rect.x + 5, self.xlim[1])
        if keys[pg.K_UP]:
            self.rect.y = max(self.rect.y - 5, self.ylim[0])
        if keys[pg.K_DOWN]:
            self.rect.y = min(self.rect.y + 5, self.ylim[1])

    def update_sprite(self):
        frame_idx = self.frame_count // self.frame_rate
        if frame_idx >= len(self.frames):
            self.frame_count = 0
            self.image = self.frames[0].convert_alpha()
        else:
            self.image = self.frames[frame_idx].convert_alpha()
        self.frame_count += 1

    # TODO: Send updated player status to the game object
    def update(self):
        self.update_sprite()
        self.update_input()
        

class Staff(pg.sprite.Sprite):
    def __init__(self, name, sprite_path, dialogue_file, width, height, pos):
        super().__init__()
        self.name = name
        self.rect = pg.Rect(pos[0], pos[1], width, height)
        self.image = pg.image.load(sprite_path).convert_alpha()
        self.dialogue_file = dialogue_file

    def update(self, patient_group):
        '''
        On collision with a patient, send dialogue text to client-side.
        '''

        # TODO: For each collided patient, start a dialogue
        hits = pg.sprite.spritecollide(self, patient_group, False)
        if len(hits) > 0:
            file = open(self.dialogue_file, "r")
            data = file.read()
            file.close()
            lines = data.split('\n')