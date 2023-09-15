import pygame as pg
from functions import spawn_lixo, draw_counter
from objects import Player
from sprite_sheet import sprites_player

fundo = pg.image.load('graphics/swamp.png')
crab = sprites_player

screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()
caranguejo = Player(400, 650, 4, int(crab[0].get_width()))
frame_count = 0

onscreen = []
counter = {'pitu': 0, 'bottle': 0, 'tire': 0}
dificuldade = 1
speed_game = 4
rodando = True
angle = 0
crab_animation = 0

while rodando:

    # Sair do jogo ao fechar a janela
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            rodando = False
            exit()

    # Spawnar um lixo
    if frame_count % 60-dificuldade == 0:
        lixo_novo = spawn_lixo(speed_game)
        onscreen.append(lixo_novo)
        
        if dificuldade > 30:
            lixo_novo = spawn_lixo(int(speed_game/2))
            onscreen.append(lixo_novo)

    # Mudar a velocidade do jogo a cade 3 segundos
    if frame_count % 180 == 0:
        speed_game += 1
        caranguejo.speed_obj = int(speed_game*1.2)

    # Aumentar o spawnrate a cada segundo
    if frame_count % 60 == 0:
        if dificuldade < 30:
            dificuldade += 1
        else:
            if frame_count % 60 == 0 and 60-dificuldade > 15:
                dificuldade += 1 

    # Mudar a animação do caranguejo a cada 0,3 segundo
    if frame_count % 20 == 0:
        image_crab, crab_animation = caranguejo.animate(crab_animation)

    
    keys = pg.key.get_pressed()
    caranguejo.move(keys)

    # draw nas surfaces
    screen.blit(fundo, (0,0))

    # desenhar apenas os lixos que não forem tocados

    removidos = []

    for item in onscreen:
        
        # mudar o angulo de pouco em pouco
        if frame_count % 3 == 0:
            angle = (angle+1)%360
        
        if item[1].y > screen.get_height():
            removidos.append(onscreen.index(item))
        
        item_rec = item[0].get_rect(topleft = (item[1].x, item[1].y))

        #Colisão de objetos
        if crab[0].get_rect(topleft = (caranguejo.x, caranguejo.y)).colliderect(item_rec):
            if item[1].sprite_id == 0:
                counter['pitu'] += 1
            elif item[1].sprite_id == 1:
                counter['bottle'] += 1
            else:
                counter['tire'] += 1
            
            print(counter)
            removidos.append(onscreen.index(item))
        
        else:

            screen.blit(pg.transform.rotate(item[0], angle+int(item[1].speed)), (item[1].x, item[1].y))
            item[1].pos_y += item[1].speed

    #Exibir counter na tela
    pitu_counter, bottle_counter, tire_counter = draw_counter(counter)
    screen.blit(pitu_counter, (25, 20))
    screen.blit(bottle_counter, (25, 50))
    screen.blit(tire_counter, (25, 80))

    screen.blit(image_crab, (caranguejo.x, caranguejo.y))
    
    # Update na tela (duh)

    pg.display.update()


    for i in removidos:
        onscreen.pop(i)
        removidos.remove(i)    
    # Contar os frames e rodar a 60FPS

    frame_count += 1

    print(clock.get_fps())
    
    clock.tick(60)