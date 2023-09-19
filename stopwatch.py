import pygame as pg
from time import time

class Stopwatch():
    
    def __init__(self, start_time):
        self._start_time = start_time
        
    def draw_stopwatch(self, screen, my_font, x_screen, image_background):
        screen.blit(image_background, (x_screen*(9/10) - 80, 15))
        screen.blit(my_font.render(f'{time() - self._start_time:.2f}', False, (255,255,255)), (x_screen*(9/10) - 40, 20))