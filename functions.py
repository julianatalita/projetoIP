from main import screen
from random import randint
from objects import Lixo
from sprite_sheet import sprite_sheet

def update_screen():
    screen.display.update()

def collision(obj1,obj2):

    if (obj2.x() < obj1.x() and obj1.x() < obj2.x() + obj2.sizex()) and (obj2.y() < obj1.y() and obj1.y() < obj2.y() + obj2.sizey()):
        return True
    else:
        return False
    
def spawn_lixo(frame, id):
    lixos = sprite_sheet[0]

    randint_id = randint(0,len(lixos)-1)
    randint_x = randint(0,screen.get_width())
    randint_y = randint(0,screen.get_height())

    obj = Lixo(randint_x, randint_y, frame, 200, 200, randint_id)

    screen.blit(obj.sprite_id(), (obj.x(), obj.y()))
    