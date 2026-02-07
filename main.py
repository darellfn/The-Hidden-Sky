import pygame
from sys import exit
from random import randint
from components.background import Background
from components.ground import Ground

pygame.init()
screen = pygame.display.set_mode((1400, 850))
pygame.display.set_caption("The Hidden Sky")


# Components
background = Background()
ground = Ground()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()

    background.get_background(screen)
    ground.get_ground(screen)
