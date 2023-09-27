import pygame as pg
from functions import draw_counter, game_diff, remove_obj, init_game, collide, draw_heart
from objects import Player
from sprite_sheet import sprites_player
from button import Button_Start, Button_Exit
from time import time
from stopwatch import Stopwatch
from music1 import Music

pg.display.init()
pg.font.init()

x_screen, y_screen, screen, clock, frame_count, onscreen, counter, dificuldade, running, angle, animation_i = init_game()

background_game = pg.image.load('graphics/swamp.png')
background_start = pg.image.load('graphics/Background.png')
background_start = pg.transform.scale(background_start, screen.get_size())
counter_box = pg.image.load('graphics/counter_background.png')
clock_box = pg.image.load('graphics/clock_background.png')
heart = pg.image.load('graphics/heart.png')
heart = pg.transform.scale(heart, (30,30))
heart_lost = pg.image.load('graphics/heart_lost.png')
heart_lost = pg.transform.scale(heart_lost, (30,30))
start = Button_Start('graphics/Button_play.png', screen)
close = Button_Exit('graphics/Button_Exit.png', screen)
crab = sprites_player
music_game = Music('musics/chico_science_maracatu_atomico.mp3')
music_start = Music('musics/start_game.mp3')

clock = pg.time.Clock()
crab_player = Player(x_screen/2-int(crab[0].get_width()), int(y_screen*0.8125), 4, int(crab[0].get_width()))

my_font = pg.font.SysFont('arial', 36)

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
        music_start.play(0)
    elif close.update():
        pg.quit()
        exit()

music_game.play(1.5)
START_TIME = time()
stopwatch = Stopwatch(START_TIME)

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
    stop_removing = False
    for item in onscreen:
        if not stop_removing:
            removidos = remove_obj(removidos, item, screen)
            if len(removidos) > 0:
                if crab_player.lose_life() == 0:
                    running = False
                stop_removing = True
            
            colididos = collide(colididos, counter, crab_player, crab, item)
            item[1].update(screen, pg.transform.rotate(item[0], item[1].obj_angle))

    stopwatch.draw_stopwatch(screen, my_font, x_screen, clock_box)

    draw_counter(counter, screen, counter_box)
    draw_heart(heart, heart_lost, crab_player._lives,screen)
    pg.display.update()

    for i in removidos:
        onscreen.remove(i)

    for i in colididos:
        onscreen.remove(i)
        colididos.remove(i)

    frame_count += 1

    clock.tick(60)
