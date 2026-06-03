import pygame
from pygame.locals import *
import UI
import main
import sys
# pygame setup
pygame.init()
screen = pygame.display.set_mode((920, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Slot Machine")
running = True
dt = 0
player_state = {
    "balance": 10000,
    "count": 0
}
images = UI.load_image()
main.start_screen(screen, images)   
btn_spin = UI.Button('Play ?',100, 100, 150, 100,lambda: main.game(screen, images,player_state)) 

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        btn_spin.handle_event(event)
    btn_spin.draw(screen)
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
