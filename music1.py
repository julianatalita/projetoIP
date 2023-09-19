import pygame as pg
import time

class Music():
    def __init__(self, music_file):
        pg.mixer.init()
        self.music = pg.mixer.Sound(music_file)
        self.muted = False

    def play(self, delay=0):
        time.sleep(delay)
        self.music.play()

    def pause(self):
        pg.mixer.pause()

    def unpause(self):
        pg.mixer.unpause()
