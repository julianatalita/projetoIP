import pygame as pg
from random import randint
from objects import Lixo
from sprite_sheet import sprite_sheet

def spawn_lixo(speed):

    width, height = pg.display.get_window_size()
    randint_x = randint(0,width-20)
    randint_y = randint(0,height/8)

    obj = Lixo(randint_x, randint_y, randint(0, 2), int(randint(int(speed/2),speed)+speed/2))

    # pra não ficar um módulo circular, é melhor dar blit(return[0], return[1])

    return [sprite_sheet[obj.sprite_id], obj]

def draw_counter(counter):
    pg.font.init()
    fonte = pg.font.Font(None, 36)
    color_font = (0,0,0)

    pitu_counter = fonte.render(f'Pitus coletados: ' + str(counter['pitu']), True, color_font)
    
    bottle_counter = fonte.render(f'Garrafas coletadas: ' + str(counter['bottle']), True, color_font)
    
    tire_counter = fonte.render(f'Pneus coletados: ' + str(counter['tire']), True, color_font)

    return pitu_counter, bottle_counter, tire_counter