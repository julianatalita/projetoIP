import pygame as pg
from functions import game_diff, remove_obj, init_game, init_sprites, draw_heart, dark_screen, finish, draw_finish
from objects import Player
from sprite_sheet import sprites_player
from button import Button_Start, Button_Exit
from time import time
from counters import Stopwatch, Points_Counter
from music1 import Music

pg.display.init()
pg.font.init()

x_screen, y_screen, screen, clock, frame_count, onscreen, dificuldade, running, angle, animation_i = init_game()

background_game, background_start, counter_box, clock_box, heart, heart_lost, start, close, crab, music_game, music_start, background_finished, play_again = init_sprites(screen, sprites_player)

clock = pg.time.Clock()
crab_player = Player(x_screen/2-int(crab[0].get_width()), int(y_screen*0.8125), 4, int(crab[0].get_width()))

my_font = pg.font.SysFont('arial', 36)

counter = Points_Counter()

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
    
    
    keys = pg.key.get_pressed()
    
    if not esc:
        frame_count, dificuldade, onscreen, speed_game = game_diff(frame_count, dificuldade, onscreen)
        animation_i = crab_player.animate(animation_i, screen, frame_count)
        crab_player.move(keys)

        removidos = []
        colididos = []
        for item in onscreen:
            removidos = remove_obj(removidos, item, screen)
            colididos = counter.collide(colididos, crab_player, crab, item)
            item[1].update(screen, pg.transform.rotate(item[0], item[1].obj_angle))
        if len(removidos) > 0:
            lives = crab_player.lose_life() 
            esc, time_record, points = finish(lives, stopwatch, time(), counter, music_game)

        stopwatch.draw_stopwatch(screen, my_font, x_screen, clock_box)

        counter.draw_counter(screen, counter_box)
        draw_heart(heart, heart_lost, crab_player._lives, screen)
        
        for i in removidos:
            onscreen.remove(i)
        for i in colididos:
            onscreen.remove(i)
    else:
        screen.blit(background_game, (0,0))
        animation_i = crab_player.animate(animation_i, screen, frame_count)
        dark_screen(screen, x_screen, y_screen)
        draw_finish(screen, background_finished, x_screen, y_screen, points, time_record)

    pg.display.update()


    frame_count += 1

    clock.tick(60)
