import pygame as pg
from time import time

class Stopwatch():
    
    def __init__(self, start_time):
        self._start_time = start_time
        
    def draw_stopwatch(self, screen, my_font, x_screen):
        screen.blit(my_font.render(f'{time() - self._start_time:.2f}', False, (0,0,0)), (x_screen*(9/10), 20))