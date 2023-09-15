import pygame as pg
from functions import spawn_lixo, draw_counter, game_diff, remove_obj
from objects import Player
from sprite_sheet import sprites_player

fundo = pg.image.load('graphics/swamp.png')
crab = sprites_player

pg.display.init()

x_screen, y_screen = pg.display.Info().current_w, pg.display.Info().current_h
screen = pg.display.set_mode((int(x_screen/2), int(3*y_screen/4)))
x_screen, y_screen = screen.get_size()

clock = pg.time.Clock()
caranguejo = Player(x_screen/2-int(crab[0].get_width()), int(y_screen*0.8125), 4, int(crab[0].get_width()))
frame_count = 0

onscreen = []
counter = {'pitu': 0, 'bottle': 0, 'tire': 0}
dificuldade = 1
rodando = True
angle = 0
crab_animation = 0

while rodando:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            rodando = False
            exit()
    
    frame_count, dificuldade, onscreen, speed_game, angle = game_diff(frame_count, dificuldade, onscreen, angle)

    if frame_count % 20 == 0:
        image_crab, crab_animation = caranguejo.animate(crab_animation)

    caranguejo.speed_obj = int(speed_game*1.2)
    
    keys = pg.key.get_pressed()
    caranguejo.move(keys)

    screen.blit(fundo, (0,0))

    removidos = []

    for item in onscreen:
        removidos = remove_obj(removidos, item, crab, screen, counter, caranguejo)
        screen.blit(pg.transform.rotate(item[0], angle+int(item[1].speed)), (item[1].x, item[1].y))
        item[1].pos_y += item[1].speed

    pitu_counter, bottle_counter, tire_counter = draw_counter(counter)
    screen.blit(pitu_counter, (25, 20))
    screen.blit(bottle_counter, (25, 50))
    screen.blit(tire_counter, (25, 80))

    screen.blit(image_crab, (caranguejo.x, caranguejo.y))

    pg.display.update()

    for i in removidos:
        onscreen.remove(i)
        removidos.remove(i)

    frame_count += 1

    clock.tick(60)  