import pygame as pg
from functions import update_screen

print('iae!')

screen = pg.display.set_mode((1600,800))

print("oi")

frame_count = 0

while True:

    # Obter as teclas pressionadas
    keys = pg.key.get_pressed()

    # Sair do jogo ao fechar a janela
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    # Update na tela (duh)
    update_screen()

    # Contar os frames e rodar a 60FPS
    frame_count += 1
    pg.time.Clock.tick(60)