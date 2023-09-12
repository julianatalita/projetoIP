import pygame as pg


screen = pg.display.set_mode((1600,800))

while True:
    keys = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()



#teste