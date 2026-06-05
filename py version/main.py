import random 
import time
from pygame.locals import *
import pygame
import sys
import sound
fruits = ["apple", "grapes", "bell", "watermelon", "cherries", "seven", "crown"]
p = [0.4, 0.2, 0.18, 0.12, 0.14, 0.04, 0.02]

def game (screen, images, player_state):
    player_state['count'] += 1
    check_balance(player_state)
    check_bet(player_state)
    end()
    result = [] 
    print("let's play slot machine")
    player_state['balance'] -= player_state['bet']
    play(screen, images, result,player_state)
    print("result :" ,result)
    if result[0] == result[1] == result[2]:
        sound.Soundmanager.sounds["win"].play()
        bingo = result[0]
        if bingo == "apple": player_state['balance'] += 2 * player_state['bet']
        elif bingo == "grapes": player_state['balance'] += 3 * player_state['bet']
        elif bingo == "bell": player_state['balance'] += 5 * player_state['bet']
        elif bingo == "watermelon": player_state['balance'] += 6 * player_state['bet']
        elif bingo == "cherries": player_state['balance'] += 7 * player_state['bet']
        elif bingo == "seven": player_state['balance'] += 9 * player_state['bet']
        elif bingo == "crown": player_state['balance'] += 13 * player_state['bet']
    print("your balance : ", player_state['balance'])
    print("your count: ", player_state['count'])
    

def random_roll(screen, images, i):
    start_time = time.perf_counter()
    while True:
        time.sleep(0.01)
        end()
        for j in range(i, 3):
            recent = random.choices(fruits, weights = p, k = 1)[0]
            x_pos = 275 + (j * 130)
            screen.blit(images[recent], (x_pos,300))

        end_time = time.perf_counter()
        elapse_time = end_time - start_time
        pygame.display.flip()
        if elapse_time >= 1.5:
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
    if player_state['count'] % 2 != 0:
        for i in range(3):
                print(f"--- Spinning reel {i + 1} ---")
                random_roll(screen, images, i)
                choice = random.choices(fruits, weights = p, k = 1)[0]
                result.append(choice)
                screen.blit(images[choice], (275 + (i * 130), 300))
                pygame.display.flip()
    else:
        choice = random.choices(fruits, weights = p, k = 1)[0]
        for i in range(3):
                print(f"--- Spinning reel {i + 1} ---")
                random_roll(screen, images, i)
                result.append(choice)
                screen.blit(images[choice], (275 + (i * 130), 300))
                pygame.display.flip()
def start_screen(screen, images):
    screen.blit(images['background'], (0, 0))
    screen.blit(images['apple'], (275 + (0 * 130), 300))
    screen.blit(images['apple'], (275 + (1 * 130), 300))
    screen.blit(images['apple'], (275 + (2 * 130), 300))
    pygame.display.flip()

def increase_bet(player_state):
    check_bet(player_state)
    if player_state['balance'] - player_state['bet'] >= 100:  
        sound.Soundmanager.sounds["cashin"].play()
        player_state['bet'] += 100
        print(player_state['bet'])
def decrease_bet(player_state):
    check_bet(player_state)
    if player_state['bet'] > 100 and player_state['balance'] > 100:
        sound.Soundmanager.sounds["cashin"].play()
        player_state['bet'] -= 100
        print(player_state['bet'])
def check_bet(player_state):
     if player_state['balance'] < player_state['bet'] :
        player_state['bet'] = player_state['balance']
def check_balance(player_state):
    if player_state['balance'] <=0:
        time.sleep(1)
        force_end()
def allin(player_state):
    sound.Soundmanager.sounds["cashin"].play()
    player_state['bet'] = player_state['balance']

