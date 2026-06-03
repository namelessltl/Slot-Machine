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
    "count": 0,
    "bet": 100
}
images = UI.load_image()
main.start_screen(screen, images)   
#Ribbon
count_ribbon = UI.Ribbon(f'Time: {player_state["count"]}', 50, 20, 150, 50)
balance_ribbon = UI.Ribbon(f'Balance: ${player_state["balance"]}', 250, 20, 250, 50)
bet_ribbon = UI.Ribbon(f'Bet: ${player_state["bet"]}', 550, 20, 150, 50)
#Button
btn_spin = UI.Button('Play ?',100, 100, 150, 100,lambda: main.game(screen, images,player_state)) 
btn_up = UI.Button('UP',450, 100, 150, 100,lambda: main.increase_bet(player_state)) 
btn_dwn = UI.Button('DOWN ',600, 100, 150, 100,lambda: main.decrease_bet(player_state)) 
btn_allin = UI.Button('All in' , 750, 100, 150, 100,lambda: main.allin(player_state))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        btn_spin.handle_event(event)
        btn_up.handle_event(event)
        btn_dwn.handle_event(event)
        btn_allin.handle_event(event)
    count_ribbon.update_text(f'Time: {player_state["count"]}')
    balance_ribbon.update_text(f'Balance: ${player_state["balance"]}')
    bet_ribbon.update_text(f'Bet: ${player_state["bet"]}')
    
    btn_spin.draw(screen)
    btn_up.draw(screen)
    btn_dwn.draw(screen)
    btn_allin.draw(screen)

    count_ribbon.draw(screen)
    balance_ribbon.draw(screen)
    bet_ribbon.draw(screen)
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
