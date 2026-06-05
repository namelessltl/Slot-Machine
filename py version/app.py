import pygame
from pygame.locals import *
import UI
import main
import sys
import sound  
# pygame setup
pygame.init()
screen = pygame.display.set_mode((920, 739))
clock = pygame.time.Clock()
pygame.display.set_caption("Slot Machine")
running = True
dt = 0
player_state = {
    "balance": 10000,
    "count": 0,
    "bet": 100
}
sound.Soundmanager.soundload()
pygame.mixer.music.play(-1)
images = UI.load_image()
main.start_screen(screen, images)   
ui_manager = UI.UImanager(screen, images, player_state)
pygame.display.set_icon(images['icon'])
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        ui_manager.handlEvent(event)
    ui_manager.update_and_draw(screen, player_state)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
