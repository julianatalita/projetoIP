import pygame as pg
from functions import spawn_lixo, draw_counter, game_diff, remove_obj, init_game
from objects import Player
from sprite_sheet import sprites_player
from button import Button_Start, Button_Exit
from time import time

pg.display.init()
pg.font.init()

x_screen, y_screen, screen, clock, frame_count, onscreen, counter, dificuldade, running, angle, animation_i = init_game()

fundo = pg.image.load('graphics/swamp.png')
background_start = pg.image.load('graphics/Background.png')
background_start = pg.transform.scale(background_start, screen.get_size())
start = Button_Start('graphics/Button_play.png', screen)
close = Button_Exit('graphics/Button_Exit.png', screen)
crab = sprites_player

clock = pg.time.Clock()
crab_player = Player(x_screen/2-int(crab[0].get_width()), int(y_screen*0.8125), 4, int(crab[0].get_width()))

my_font = pg.font.SysFont('arial', 40)

while not running:
    screen.blit(background_start, (0,0))
    start.draw_button()
    close.draw_button()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False
            exit()
    
    pg.display.update()

    if start.update():
        running = True
        START_TIME = time()
    elif close.update():
        pg.quit()
        exit()

while running:

    screen.blit(fundo, (0,0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            running = False
            exit()
    
    frame_count, dificuldade, onscreen, speed_game = game_diff(frame_count, dificuldade, onscreen)

    animation_i = crab_player.animate(animation_i, screen, frame_count)
    
    keys = pg.key.get_pressed()
    crab_player.move(keys)

    removidos = []
    for item in onscreen:
        removidos = remove_obj(removidos, item, crab, screen, counter, crab_player)
        item[1].update(screen, pg.transform.rotate(item[0], item[1].obj_angle))

    screen.blit(my_font.render(str((time() - START_TIME)), False, (0,0,0)), (750, 20))

    draw_counter(counter, screen)

    pg.display.update()

    for i in removidos:
        onscreen.remove(i)
        removidos.remove(i)

    frame_count += 1

    clock.tick(60)  