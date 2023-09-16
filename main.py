import pygame as pg
from functions import draw_counter, game_diff, remove_obj, init_game
from objects import Player
from sprite_sheet import sprites_player

fundo = pg.image.load('graphics/swamp.png')
crab = sprites_player
pg.display.init()

x_screen, y_screen, screen, clock, frame_count, onscreen, counter, dificuldade, running, angle, crab_animation = init_game()

crab_player = Player(x_screen/2-int(crab[0].get_width()), int(y_screen*0.8125), 4, int(crab[0].get_width()))

while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False
            exit()
    
    frame_count, dificuldade, onscreen, speed_game, angle = game_diff(frame_count, dificuldade, onscreen, angle)

    if frame_count % 20 == 0:
        image_crab, crab_animation = crab_player.animate(crab_animation)

    crab_player.speed_obj = int(speed_game*1.2)
    
    keys = pg.key.get_pressed()
    crab_player.move(keys)

    screen.blit(fundo, (0,0))

    removidos = []

    for item in onscreen:
        removidos = remove_obj(removidos, item, crab, screen, counter, crab_player)
        screen.blit(pg.transform.rotate(item[0], angle+int(item[1].speed)), (item[1].x, item[1].y))
        item[1].pos_y += item[1].speed

    draw_counter(counter, screen)

    screen.blit(image_crab, (crab_player.x, crab_player.y))

    pg.display.update()

    for i in removidos:
        onscreen.remove(i)
        removidos.remove(i)

    frame_count += 1

    clock.tick(60)  