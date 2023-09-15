import pygame as pg
from random import randint
from objects import Lixo
from sprite_sheet import sprite_sheet

def spawn_lixo(speed):

    width, height = pg.display.get_window_size()

    randint_x = randint(width/8,int(7*width/8))
    randint_y = randint(0,int(height/8))

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

def game_diff(frame_count, dificuldade, onscreen):
    
    speed_game = 4 + int(frame_count/180)

    if frame_count % 60-dificuldade == 0:
        lixo_novo = spawn_lixo(speed_game)
        onscreen.append(lixo_novo)
        
        if dificuldade > 30:
            lixo_novo = spawn_lixo(int(speed_game/2))
            onscreen.append(lixo_novo)

    # Aumentar o spawnrate a cada segundo
    if frame_count % 60 == 0:
        if dificuldade < 30:
            dificuldade += 1
        else:
            if frame_count % 60 == 0 and 60-dificuldade > 15:
                dificuldade += 1 

    return frame_count, dificuldade, onscreen, speed_game
    
