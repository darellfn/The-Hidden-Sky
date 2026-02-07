import pygame
from sys import exit
from random import randint
from components.background import Background
from components.ground import Ground
from characters.player import Player

pygame.init()
screen = pygame.display.set_mode((1400, 850))
pygame.display.set_caption("The Hidden Sky")

# Components
background = Background()
ground = Ground()

# Player
player = Player()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    player.movement(keys)

    background.get_background(screen)
    ground.get_ground(screen)
    player.get_player(screen)

    pygame.display.update()