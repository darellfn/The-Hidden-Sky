import pygame
from sys import exit
from random import randint
from components.background import Background
from components.ground import Ground
from characters.player import Player
from components.platform import Platform
from levels.level_1 import Level_1
from levels.level_2 import Level_2


pygame.init()
screen = pygame.display.set_mode((1400, 850))
pygame.display.set_caption("The Hidden Sky")
clock = pygame.time.Clock()

# Levels

level_1 = Level_1(screen)
level_2 = Level_2(screen)

level_1_unlocked = True
level_2_unlocked = False
level_3_unlocked = False
level_4_unlocked = False
level_5_unlocked = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # if level_1_unlocked:
    #     level_1.start()
        
    #     if level_1.is_finished():
    level_2_unlocked = True
        
    if level_2_unlocked:
        level_2.start()

            # if level_2.is_finished():

            # if level_3_unlocked:
            #     level_3.start()
        
    pygame.display.update()

    clock.tick(60)