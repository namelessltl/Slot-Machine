import pygame
import sys
import os
class Soundmanager:
    sounds = {}
    @classmethod
    def soundload(cls):
        # pygame.mixer.init()
        cls.sounds['cashin'] = pygame.mixer.Sound(os.path.join('assest', 'cashin.wav'))
        cls.sounds['win'] = pygame.mixer.Sound(os.path.join('assest', 'win.wav'))
        
        pygame.mixer.music.load(os.path.join('assest', 'em_background.mp3'))