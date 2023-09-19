import pygame as pg
from random import randint
from objects import Lixo
from sprite_sheet import sprite_sheet
from math import log2

def spawn_lixo(frame_count):

    width, height = pg.display.get_window_size()

    randint_x = randint(width//6,int(5*width//6))
    randint_y = randint(0,int(height/16))

    obj = Lixo(randint_x, randint_y, randint(0, 2), frame_count)

    # pra não ficar um módulo circular, é melhor dar blit(return[0], return[1])

    return [sprite_sheet[obj.sprite_id], obj]

def draw_counter(counter, screen):

    pg.font.init()
    fonte = pg.font.Font(None, 36)
    color_font = (0,0,0)

    pitu_counter = fonte.render(f'Pitus coletados: ' + str(counter['pitu']), True, color_font)
    
    bottle_counter = fonte.render(f'Garrafas coletadas: ' + str(counter['bottle']), True, color_font)
    
    tire_counter = fonte.render(f'Pneus coletados: ' + str(counter['tire']), True, color_font)

    screen.blit(pitu_counter, (25, 20))

    screen.blit(bottle_counter, (25, 50))

    screen.blit(tire_counter, (25, 80))

def game_diff(frame_count, dificuldade, onscreen):

    speed_game = int(log2(4 + int(frame_count/300)))

    dificuldade = int(log2(1 + int(frame_count/360)))+1

    if frame_count % int(60/(dificuldade/1.5)) == 0 and len(onscreen) < 1 + dificuldade * 1.1:
        lixo_novo = spawn_lixo(frame_count)
        onscreen.append(lixo_novo)

    # Aumentar o spawnrate a cada segundo
    
    return frame_count, dificuldade, onscreen, speed_game
    
def remove_obj(removidos, item, crab, screen, counter, crab_player):
    if item[1].y > screen.get_height():
        removidos.append(item)

    item_rec = item[0].get_rect(topleft = (item[1].x, item[1].y))

    if crab[0].get_rect(topleft = (crab_player.x, crab_player.y)).colliderect(item_rec):
        if item[1].sprite_id == 0:
            counter['pitu'] += 1
        elif item[1].sprite_id == 1:
            counter['bottle'] += 1
        else:
            counter['tire'] += 1
            
        print(counter)
        removidos.append(item)
    
    return removidos

def init_game():
    pg.display.init()
    x_screen, y_screen = pg.display.Info().current_w, pg.display.Info().current_h
    screen = pg.display.set_mode((int(x_screen/2), int(3*y_screen/4)))
    x_screen, y_screen = screen.get_size()

    clock = pg.time.Clock()
    
    frame_count = 0

    onscreen = []
    counter = {'pitu': 0, 'bottle': 0, 'tire': 0}
    dificuldade = 1
    running = False
    angle = 0
    crab_animation = 0
    return x_screen, y_screen, screen, clock, frame_count, onscreen, counter, dificuldade, running, angle, crab_animation