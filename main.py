import pygame as pg
from functions import draw_counter, game_diff, remove_obj, init_game, init_sprites, collide, draw_heart, dark_screen
from objects import Player
from sprite_sheet import sprites_player
from button import Button_Start, Button_Exit
from time import time
from stopwatch import Stopwatch
from music1 import Music

pg.display.init()
pg.font.init()

x_screen, y_screen, screen, clock, frame_count, onscreen, counter, dificuldade, running, angle, animation_i = init_game()

background_game, background_start, counter_box, clock_box, heart, heart_lost, start, close, crab, music_game, music_start = init_sprites(screen, sprites_player)

clock = pg.time.Clock()
crab_player = Player(x_screen/2-int(crab[0].get_width()), int(y_screen*0.8125), 4, int(crab[0].get_width()))

my_font = pg.font.SysFont('arial', 36)

while not running:

    screen.fill([255,255,255])

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
        music_start.play(0)
    elif close.update():
        pg.quit()
        exit()

music_game.play(1.5)
START_TIME = time()
stopwatch = Stopwatch(START_TIME)

esc = False
while running:

    screen.blit(background_game, (0,0))
    
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
    colididos = []
    for item in onscreen:
        removidos = remove_obj(removidos, item, screen)
        colididos = collide(colididos, counter, crab_player, crab, item)
        item[1].update(screen, pg.transform.rotate(item[0], item[1].obj_angle))
    if len(removidos) > 0:
        if crab_player.lose_life() == 0:
            #running = False
            esc = True


    stopwatch.draw_stopwatch(screen, my_font, x_screen, clock_box)

    draw_counter(counter, screen, counter_box)
    draw_heart(heart, heart_lost, crab_player._lives,screen)
    
    if esc:
        dark_screen(screen, x_screen, y_screen)

    pg.display.update()

    for i in removidos:
        onscreen.remove(i)
    for i in colididos:
        onscreen.remove(i)

    frame_count += 1

    clock.tick(60)
