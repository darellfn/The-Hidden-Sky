import pygame
from sys import exit
from random import randint
from components.background import Background
from components.ground import Ground
from characters.player import Player
from components.platform import Platform
from levels.level_1 import Level_1

pygame.init()
screen = pygame.display.set_mode((1400, 850))
pygame.display.set_caption("The Hidden Sky")

# Levels

level_1 = Level_1(screen)

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

    if level_1:
        level_1.start()
        

    pygame.display.update()