import pygame as pg
from random import randint
from objects import Lixo
from button import Button_Start, Button_Exit, Button_Play_Again
from sprite_sheet import sprite_sheet
from math import log2
from music1 import Music

def spawn_lixo(frame_count):

    width, height = pg.display.get_window_size()

    randint_x = randint(width//6,int(5*width//6))
    randint_y = randint(0,int(height/16))

    obj = Lixo(randint_x, randint_y, randint(0, 2), frame_count)

    # pra não ficar um módulo circular, é melhor dar blit(return[0], return[1])

    return [sprite_sheet[obj.sprite_id], obj]

def draw_counter(counter, screen, image_background):

    pg.font.init()
    fonte = pg.font.Font(None, 30)
    color_font = (255,255,255)
    
    pitu_counter = fonte.render(f'Pitus: ' + str(counter['pitu']), True, color_font)
    
    bottle_counter = fonte.render(f'Garrafas: ' + str(counter['bottle']), True, color_font)
    
    tire_counter = fonte.render(f'Pneus: ' + str(counter['tire']), True, color_font)
 
    screen.blit(image_background, (5,10))
    screen.blit(pitu_counter, (25,25))

    screen.blit(image_background, (5,50))
    screen.blit(bottle_counter, (25, 65))

    screen.blit(image_background, (5,90))
    screen.blit(tire_counter, (25, 105))

def game_diff(frame_count, dificuldade, onscreen):

    speed_game = int(log2(4 + int(frame_count/300)))

    dificuldade = int(log2(1 + int(frame_count/360)))+1

    if frame_count % int(60/(dificuldade/1.5)) == 0 and len(onscreen) < 1 + dificuldade * 1.1:
        lixo_novo = spawn_lixo(frame_count)
        onscreen.append(lixo_novo)

    # Aumentar o spawnrate a cada segundo
    
    return frame_count, dificuldade, onscreen, speed_game
    
def remove_obj(removidos, item, screen):
  if item[1].y > screen.get_height():
    removidos.append(item)
  return removidos

def collide(colididos, counter, crab_player, crab, item):
  item_rec = item[0].get_rect(topleft=(item[1].x, item[1].y))
  crab_rec = crab[0].get_rect(topleft=(crab_player.x, crab_player.y))

  if crab_rec.colliderect(item_rec):
    if item[1].sprite_id == 0:
      counter['pitu'] += 1
    elif item[1].sprite_id == 1:
      counter['bottle'] += 1
    else:
      counter['tire'] += 1

    colididos.append(item)

  return colididos

def init_game():
    pg.display.init()
    x_screen, y_screen = pg.display.Info().current_w, pg.display.Info().current_h
    screen = pg.display.set_mode((int(x_screen/2), int(3*y_screen/4)))
    pg.display.set_caption('MangueBit')
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

def init_sprites(screen, sprites_player):

  background_game = pg.image.load('graphics/swamp.png')
  background_game = pg.transform.scale(background_game, screen.get_size())
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
  play_again = Button_Play_Again('graphics/Button_play_again.png', screen)

  crab = sprites_player
  pg.display.set_icon(crab[0])

  music_game = Music('musics/chico_science_maracatu_atomico.mp3')
  music_start = Music('musics/start_game.mp3')

 

  return background_game, background_start, counter_box, clock_box, heart, heart_lost, start, close, crab, music_game, music_start, play_again

def draw_heart(image_on, image_off, lives, screen):
  x_screen = screen.get_width()
  for c in range(3):
    if c + 1 <= lives:
      screen.blit(image_on, ((x_screen) * 9/10 - 68 + 40 * c, 75))
    else:
      screen.blit(image_off, ((x_screen) * 9/10 - 68 + 40 * c, 75)) 


def dark_screen(surface, wid, height, alpha=150):
    overlay = pg.Surface((wid, height), pg.SRCALPHA)
    overlay.fill((0, 0, 0, alpha))
    surface.blit(overlay, (0, 0))
    

def finish(lives, stopwatch, time, counter, music):
  if lives == 0:
    time_record = time - stopwatch._start_time
    points = 0
    for v in counter.values():
        points += v
    print(f'{time_record:.2f}')
    print(counter, points)
    music.pause()
    
    return True