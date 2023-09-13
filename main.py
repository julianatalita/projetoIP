import pygame as pg
from functions import spawn_lixo
from objects import Player

screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()
caranguejo = Player(400, 650, 4)
frame_count = 0

fundo = pg.image.load('graphics/swamp.png')
crab = pg.image.load('graphics/crab.png')

onscreen = []
contador = {'pitu': 0, 'garrafa': 0, 'pneu': 0}
dificuldade = 1
speed_game = 4
rodando = True

while rodando:

    # Sair do jogo ao fechar a janela
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            rodando = False
            exit()

    # Spawnar um lixo a cada 2 segundos (120 frames)
    if frame_count % 60-dificuldade == 0:
        lixo_novo = spawn_lixo(speed_game)
        onscreen.append(lixo_novo)

    # Mudar a velocidade do jogo a cade 3 segundos
    if frame_count % 180 == 0:
        speed_game += 1
        caranguejo.speed_obj = int(speed_game*1.2)

    # Aumentar o spawnrate a cada meio segundo
    if frame_count % 30 == 0 and dificuldade > 30:
        dificuldade += 1
        print(dificuldade)

    keys = pg.key.get_pressed()
    caranguejo.move(keys)

    # draw nas surfaces
    screen.blit(fundo, (0,0))

    # desenhar apenas os lixos que não forem tocados

    for item in onscreen:
        item_rec = item[0].get_rect(topleft = (item[1].x, item[1].y))
        if crab.get_rect(topleft = (caranguejo.x, caranguejo.y)).colliderect(item_rec):
            if item[1].sprite_id == 0:
                contador['pitu'] += 1
            elif item[1].sprite_id == 1:
                contador['garrafa'] += 1
            else:
                contador['pneu'] += 1
            
            print(contador)
            onscreen.remove(item)
        else:
            screen.blit(item[0], (item[1].x, item[1].y))
            item[1].pos_y += item[1].speed


    screen.blit(crab, (caranguejo.x, caranguejo.y))
    
    # Update na tela (duh)

    pg.display.update()

    # Contar os frames e rodar a 60FPS

    frame_count += 1

    clock.tick(60)