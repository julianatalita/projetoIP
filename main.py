import pygame as pg
from functions import spawn_lixo, move, collision
from objects import Player

screen = pg.display.set_mode((1600,800))
clock = pg.time.Clock()
carangueijo = Player(800, 400, 100, 100)
frame_count = 0

fundo = pg.image.load('graphics/swamp.png')
crab = pg.image.load('graphics/crab.png')

onscreen = []

while True:

    # Sair do jogo ao fechar a janela
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    # Spawnar um lixo a cada 2 segundos (120 frames)
    if frame_count % 120 == 0:
        lixo_novo = spawn_lixo(frame_count)
        onscreen.append(lixo_novo)

    carangueijo.pos_x, carangueijo.pos_y = move(carangueijo.x, carangueijo.y)

    # draw nas surfaces
    screen.blit(fundo, (0,0))

    # desenhar apenas os lixos que não forem tocados

    for item in onscreen:
        if collision(carangueijo, item[1]) or collision(item[1],carangueijo):
            onscreen.remove(item)
        else:
            screen.blit(item[0], (item[1].x, item[1].y))
            
    screen.blit(crab, (carangueijo.x, carangueijo.y))
    
    # Update na tela (duh)

    pg.display.update()

    # Contar os frames e rodar a 60FPS

    frame_count += 1
    print(frame_count)
    clock.tick(60)