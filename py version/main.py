import random 
import time
from pygame.locals import *
import pygame
import sys

fruits = ["apple", "grapes", "bell", "watermelon", "cherries", "seven", "crown"]
p = [0.3, 0.16, 0.14,0.13,0.1,0.9, 0.8]
def game (screen, images, player_state):
    player_state['count'] += 1
    if player_state['balance'] <=0:
        time.sleep(1)
        force_end()
    end()
    result = [] 
    print("let's play slot machine")
    bet = 500
    player_state['balance'] -= bet
    play(screen, images, result,player_state)
    print("result :" ,result)
    if result[0] == result[1] == result[2]:
        bingo = result[0]
        if bingo == "apple": player_state['balance'] += 2000
        elif bingo == "grapes": player_state['balance'] += 3000
        elif bingo == "bell": player_state['balance'] += 5000
        elif bingo == "watermelon": player_state['balance'] += 6000
        elif bingo == "cherries": player_state['balance'] += 7000
        elif bingo == "seven": player_state['balance'] += 77777
        elif bingo == "crown": player_state['balance'] += 100000

    print("your balance : ", player_state['balance'])
    print("your count: ", player_state['count'])
    

def random_roll(screen, images, i):
    start_time = time.perf_counter()
    while True:
        time.sleep(0.1)
        end()
        for j in range(i, 3):
            recent = random.choices(fruits, weights = p, k = 1)[0]
            x_pos = 300 + (j * 150)
            screen.blit(images[recent], (x_pos,270))

        end_time = time.perf_counter()
        elapse_time = end_time - start_time
        pygame.display.flip()
        if elapse_time >= 2.0:
            break

def end():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def force_end():
    pygame.quit()
    sys.exit()
def play(screen, images, result, player_state):
    if player_state['count'] % 5 != 0:
        for i in range(3):
                print(f"--- Spinning reel {i + 1} ---")
                random_roll(screen, images, i)
                choice = random.choices(fruits, weights = p, k = 1)[0]
                result.append(choice)
                screen.blit(images[choice], (300 + (i * 150), 270))
                pygame.display.flip()
    else:
        choice = random.choices(fruits, weights = p, k = 1)[0]
        for i in range(3):
                print(f"--- Spinning reel {i + 1} ---")
                random_roll(screen, images, i)
                result.append(choice)
                screen.blit(images[choice], (300 + (i * 150), 270))
                pygame.display.flip()
def start_screen(screen, images):
    screen.blit(images['background'], (0, 0))
    screen.blit(images['apple'], (300 + (0 * 150), 270))
    screen.blit(images['apple'], (300 + (1 * 150), 270))
    screen.blit(images['apple'], (300 + (2 * 150), 270))
    pygame.display.flip()