import pygame as pg
from random import randint
from objects import Lixo

def collision(obj1,obj2):
    #cada objeto tem uma posição e um tamanho, se eles estiverem colidindo, algum vai estar "entre" as cordenadas dos 2

    if (obj2.x < obj1.x and obj1.x < obj2.x + obj2.sizex) and (obj2.y < obj1.y and obj1.y < obj2.y + obj2.sizey):
        return True
    else:
        return False

def spawn_lixo(frame):

    width, height = pg.display.get_window_size()
    randint_x = randint(0,width)
    randint_y = randint(0,height)

    # a próxima linha inicia um lixo em uma posição aleatória no frame que é fornecido à função (usado para saber se é pra renderizar o lixo ou não)
    # 200,200,0 é por que ainda só tem 1 tipo de lixo

    obj = Lixo(randint_x, randint_y, frame, 200, 200, 0)

    # pra não ficar um módulo circular, é melhor dar blit(return[0], return[1])

    return (pg.image.load('graphics/sacola.png'), obj)

def move(x, y):
    keys = pg.key.get_pressed()

    if keys[pg.K_w]:
        y -= 3
    if keys[pg.K_a]:
        x -= 3
    if keys[pg.K_s]:
        y += 3
    if keys[pg.K_d]:
        x += 3
    
    return (x,y)
