import pygame as pg
from random import randint
from objects import Lixo

def spawn_lixo(frame, speed):

    width, height = pg.display.get_window_size()
    randint_x = randint(0,width)
    randint_y = randint(0,height/8)

    # a próxima linha inicia um lixo em uma posição aleatória no frame que é fornecido à função (usado para saber se é pra renderizar o lixo ou não)
    # 122,177,0 é por que ainda só tem 1 tipo de lixo

    obj = Lixo(randint_x, randint_y, frame, 122, 177, 0, int(randint(int(speed/2),speed)+speed/2))

    # pra não ficar um módulo circular, é melhor dar blit(return[0], return[1])

    return [pg.image.load('graphics/sacola.png'), obj]


