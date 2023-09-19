import pygame as pg
from abc import ABC

#button class
class Button(ABC):
    def __init__(self, image_id, screen):
        self.image = pg.image.load(image_id)
        self.screen = screen
        self.x_screen, self.y_screen = self.screen.get_size()

    def update(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            return self.check_if_click()

    def check_if_click(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pressed()[0]:
                return True

class Button_Start(Button):

    def __init__(self, image, screen):
        super().__init__(image, screen)
        self.rect = self.image.get_rect(topleft = ((self.x_screen//2) - self.image.get_width()//2,self.y_screen*3//5))

    def draw_button(self):
        self.screen.blit(self.image, ((self.x_screen//2) - self.image.get_width()//2,self.y_screen*3//5))

    def update(self):
        return super().update()

    def check_if_click(self):
        return super().check_if_click()

class Button_Exit(Button):

    def __init__(self, image, screen):
        super().__init__(image, screen)
        self.rect = self.image.get_rect(topleft = ((self.x_screen//2) - self.image.get_width()//2,self.y_screen*3//5 + 85))


    def draw_button(self):
        x_screen, y_screen = self.screen.get_size()
        self.screen.blit(self.image, ((x_screen//2) - self.image.get_width()//2,y_screen*3//5 + 85))

    def update(self):
        super().update()

    def check_if_click(self):
        super().check_if_click()
    
    def update(self):
        return super().update()

    def check_if_click(self):
        return super().check_if_click()