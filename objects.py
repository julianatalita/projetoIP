import pygame as pg

class Lixo:

    # Iniciar com x, y, frame que a sacola foi gerada, largura do sprite, altura do sprite, id (ignorar por enquanto, é pra ser uma spritesheet dps)

    def __init__(self, pos_x, pos_y, frame_start, size_x, size_y, id, speed_obj):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.frame_start = frame_start
        self.size_x = size_x
        self.size_y = size_y
        self.id = id
        self.speed_obj = speed_obj
    
    @property
    def x(self):
        return self.pos_x
    
    @property
    def y(self):
        return self.pos_y
    
    @property
    def startframe(self):
        return self.frame_start
    
    @property
    def sizex(self):
        return self.size_x
    
    @property
    def sizey(self):
        return self.size_y
    
    @property
    def sprite_id(self):
        return self.id

    @property
    def speed(self):
        return self.speed_obj
    

class Player:

    # O player por enquanto é só x, y, largura da imagem e altura da imagem

    def __init__(self, pos_x, pos_y, size_x, size_y, speed_obj):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.speed_obj = speed_obj

    @property
    def x(self):
        return self.pos_x
    
    @property
    def y(self):
        return self.pos_y
    
    @property
    def sizex(self):
        return self.size_x
    
    @property
    def sizey(self):
        return self.size_y
    
    @property
    def speed(self):
        return self.speed_obj

    def move(self, direcao):
        if direcao[pg.K_d]:
            self.pos_x += self.speed
        if direcao[pg.K_a]:
            self.pos_x -= self.speed
