import pygame
from pygame.locals import *
import os 
import main

def load_image():

    images = {}
    
    images['background'] = pygame.image.load(os.path.join('assest','background.jpg')).convert()

    icon_size = (80, 80)
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
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)


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

class Ribbon:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        
        # Font setup
        self.font = pygame.font.SysFont("Arial", 30)
        self.text_surf = self.font.render(self.text, True, WHITE)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def update_text(self, new_text):
        if self.text != new_text: 
            self.text = new_text
            self.text_surf = self.font.render(self.text, True, WHITE)
            self.text_rect = self.text_surf.get_rect(center=self.rect.center)
            
    def draw(self, surface):
        current_color = GREEN
        pygame.draw.rect(surface, current_color, self.rect, border_radius=8)
        surface.blit(self.text_surf, self.text_rect) 
    

class UImanager:
    def __init__(self, screen, images, player_state):
        #Ribbon
        self.count_ribbon = Ribbon(f'Time: {player_state["count"]}', 50, 20, 150, 50)
        self.balance_ribbon = Ribbon(f'Balance: ${player_state["balance"]}', 250, 20, 250, 50)
        self.bet_ribbon = Ribbon(f'Bet: ${player_state["bet"]}', 550, 20, 150, 50)
        #Button
        self.btn_spin = Button('Spin',365, 475, 160, 70,lambda: main.game(screen, images,player_state)) 
        self.btn_up = Button('UP',700, 200, 150, 100,lambda: main.increase_bet(player_state)) 
        self.btn_dwn = Button('DOWN ',700, 305, 150, 100,lambda: main.decrease_bet(player_state)) 
        self.btn_allin = Button('All in' , 700, 410, 150, 100,lambda: main.allin(player_state))
    def handlEvent(self, event):
        self.btn_spin.handle_event(event)
        self.btn_up.handle_event(event)
        self.btn_dwn.handle_event(event)
        self.btn_allin.handle_event(event)
    def update_and_draw(self, screen, player_state):
        self.count_ribbon.update_text(f'Time: {player_state["count"]}')
        self.balance_ribbon.update_text(f'Balance: ${player_state["balance"]}')
        self.bet_ribbon.update_text(f'Bet: ${player_state["bet"]}')
        
        self.btn_spin.draw(screen)
        self.btn_up.draw(screen)
        self.btn_dwn.draw(screen)
        self.btn_allin.draw(screen)

        self.count_ribbon.draw(screen)
        self.balance_ribbon.draw(screen)
        self.bet_ribbon.draw(screen)