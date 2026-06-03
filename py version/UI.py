import pygame
from pygame.locals import *
import os 

def load_image():

    images = {}
    
    images['background'] = pygame.image.load(os.path.join('assest','background.jpg')).convert()

    icon_size = (120, 120)
    apple = pygame.image.load(os.path.join('assest','apple.png')).convert()
    images['apple'] = pygame.transform.scale(apple, icon_size)
    bell = pygame.image.load(os.path.join('assest','bell.png')).convert()
    images['bell'] = pygame.transform.scale(bell, icon_size)
    cherries = pygame.image.load(os.path.join('assest','cherries.png')).convert()
    images['cherries'] = pygame.transform.scale(cherries, icon_size)
    seven = pygame.image.load(os.path.join('assest','seven.png')).convert()
    images['seven'] = pygame.transform.scale(seven, icon_size)
    watermelon = pygame.image.load(os.path.join('assest','watermelon.png')).convert()
    images['watermelon'] = pygame.transform.scale(watermelon, icon_size)
    crown = pygame.image.load(os.path.join('assest','crown.png')).convert()
    images['crown'] = pygame.transform.scale(crown, icon_size)
    grapes = pygame.image.load(os.path.join('assest','grapes.png')).convert()
    images['grapes'] = pygame.transform.scale(grapes, icon_size)
    
    return images

clock = pygame.time.Clock()

# Color Definitions
WHITE = (255, 255, 255)
BG_COLOR = (30, 30, 40)
BUTTON_COLOR = (50, 150, 250)
HOVER_COLOR = (100, 180, 255)

class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback
        
        # Font setup
        self.font = pygame.font.SysFont("Arial", 30)
        self.text_surf = self.font.render(self.text, True, WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)
        
        # Debounce state tracking
        self.clicked = False

    def draw(self, surface):
        # 1. Check for hover state
        mouse_pos = pygame.mouse.get_pos()
        current_color = HOVER_COLOR if self.rect.collidepoint(mouse_pos) else BUTTON_COLOR
        
        # 2. Render button and text
        pygame.draw.rect(surface, current_color, self.rect, border_radius=8)
        surface.blit(self.text_surf, self.text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()