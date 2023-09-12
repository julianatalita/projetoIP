from main import screen

def update_screen():
    screen.display.update()

def collision(obj1,obj2):
    if (obj2.x() < obj1.x() and obj1.x() < obj2.x() + obj2.sizex()) and (obj2.y() < obj1.y() and obj1.y() < obj2.y() + obj2.sizey()):
        return True
    else:
        return False