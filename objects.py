import pygame as pg
from sprite_sheet import sprite_sheet
from abc import ABC
from random import randint
from math import log2

class Positions(ABC):
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
    
    

class Lixo(Positions):

    # Iniciar com x, y, id e velocidade
    def __init__(self, pos_x, pos_y, id, frame_count):
        super().__init__(pos_x, pos_y)
        self.id = id
        self.frame_count = frame_count
        self.angle = randint(0,360)
        const = 4 + int(self.frame_count/180)
        self.speed_obj = int(randint(int(const/2),int(3*const/4))+const/5)
    
    @property
    def x(self):
        return self.pos_x
    
    @property
    def y(self):
        return self.pos_y
    
    @property
    def sprite_id(self):
        return self.id

    @property
    def speed(self):
        return self.speed_obj
    
    @property
    def obj_angle(self):
        return self.angle
    
    def update(self, screen, img):
        self.angle += 1
        self.pos_y += self.speed
        self.draw(screen, img)
    
    def draw(self, screen, img):
        screen.blit(img, (self.x, self.y))


class Player(Positions):

    # O player por enquanto é só x, y e largura dele
    def __init__(self, pos_x, pos_y, speed_obj, width):
        super().__init__(pos_x, pos_y)
        self.speed_obj = speed_obj
        self.width = width
        self.lives = 3
        
    @property
    def x(self):
        return self.pos_x
    
    @property
    def y(self):
        return self.pos_y
    
    @property
    def speed(self):
        return self.speed_obj

    @property
    def player_width(self):
        return self.width
    
    @property
    def _lives(self):
        return self.lives

    def move(self, direcao):
        if direcao[pg.K_d] and self.x < pg.display.get_window_size()[0] - self.player_width:
            self.pos_x += self.speed
            if self.pos_x > pg.display.get_window_size()[0] - self.player_width:
                self.pos_x = pg.display.get_window_size()[0] - self.player_width
        if direcao[pg.K_a] and self.x > 0:
            self.pos_x -= self.speed
            if self.pos_x < 0:
                self.pos_x = 0
    
    def animate(self, animation_i, screen, frame_count):

        self.speed_obj = 1+(int(frame_count/180))

        if frame_count % 20 == 0:
            animation_i = (animation_i+1)% len(sprite_sheet[5])
            
        screen.blit(sprite_sheet[5][animation_i], (self.x, self.y))
        return animation_i
    
    def lose_life(self):
        self.lives -= 1
        print(self._lives)
        return self._lives
        
    def game_over(self):
        return False
