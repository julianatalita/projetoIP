import pygame as pg

#button class
class Button():

    def __init__(self, image, screen):
        self.image = pg.image.load(image)
        self.screen = screen


class Button_Start(Button):

    def __init__(self, image, screen):
        super().__init__(image, screen)

    def draw_button(self):
        x_screen, y_screen = self.screen.get_size()
        self.screen.blit(self.image, ((x_screen//2) - self.image.get_width()//2,y_screen*3//5))


class Button_Exit(Button):

    def __init__(self, image, screen):
        super().__init__(image, screen)

    def draw_button(self):
        x_screen, y_screen = self.screen.get_size()
        self.screen.blit(self.image, ((x_screen//2) - self.image.get_width()//2,y_screen*3//5 + 85))
