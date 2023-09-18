import pygame as pg
from functions import draw_counter, game_diff, remove_obj, init_game
from objects import Player
from sprite_sheet import sprites_player

fundo = pg.image.load('graphics/swamp.png')
crab = sprites_player
pg.display.init()

x_screen, y_screen, screen, clock, frame_count, onscreen, counter, dificuldade, running, angle, crab_animation = init_game()

crab_player = Player(x_screen/2-int(crab[0].get_width()), int(y_screen*0.8125), 4, int(crab[0].get_width()))
frame_count = 0

onscreen = []
counter = {'pitu': 0, 'bottle': 0, 'tire': 0}
dificuldade = 1
running = True
animation_i = 0

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False
            exit()
    
    screen.blit(fundo, (0,0))

    frame_count, dificuldade, onscreen, speed_game = game_diff(frame_count, dificuldade, onscreen)
    
    keys = pg.key.get_pressed()
    crab_player.move(keys)

    removidos = []
    
    for item in onscreen:
        removidos = remove_obj(removidos, item, crab, screen, counter, crab_player)
        item[1].update(screen, pg.transform.rotate(item[0], item[1].obj_angle))

    animation_i = crab_player.animate(animation_i, screen, frame_count)

    draw_counter(screen, counter)

    pg.display.update()

    for i in removidos:
        onscreen.remove(i)
        removidos.remove(i)

    frame_count += 1

    clock.tick(60)  