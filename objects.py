import pygame as pg
from sprite_sheet import sprite_sheet
from abc import ABC
from random import randint

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
        
        const = 4 + int(self.frame_count/180)
        self.speed_obj = int(randint(int(const/2),const)+const/2)
    
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
    

class Player(Positions):

    # O player por enquanto é só x, y e largura dele
    def __init__(self, pos_x, pos_y, speed_obj, width):
        super().__init__(pos_x, pos_y)
        self.speed_obj = speed_obj
        self.width = width
        
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

    def move(self, direcao):
        if direcao[pg.K_d] and self.x < pg.display.get_window_size()[0] - self.player_width:
            self.pos_x += self.speed
            if self.pos_x > pg.display.get_window_size()[0] - self.player_width:
                self.pos_x = pg.display.get_window_size()[0] - self.player_width
        if direcao[pg.K_a] and self.x > 0:
            self.pos_x -= self.speed
            if self.pos_x < 0:
                self.pos_x = 0
    
    def animate(self, animation_i):
        animation_i = (animation_i+1)% len(sprite_sheet[5])
        return sprite_sheet[5][animation_i], animation_i