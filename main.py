import pygame as pg
from functions import update_screen

print('iae, mermãozão!')

screen = pg.display.set_mode((1600,800))

print("oi")
print("abcde")

frame_count = 0
print('to feliz')

while True:

    # Obter as teclas pressionadas
    keys = pg.key.get_pressed()

    # Sair do jogo ao fechar a janela
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()