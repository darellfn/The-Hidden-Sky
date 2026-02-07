import pygame

class Enemy:
    def __init__(self, y):
        super().__init__
        self.enemy_size = (100, 100)
        self.y = y

        self.enemy_image = pygame.image.load("graphics/characters/enemies/swat.png").convert_alpha()
        self.enemy_image = pygame.transform.scale(self.enemy_image, (self.enemy_size))
        self.enemy_rect = self.enemy_image.get_rect(midbottom = (100, self.y))

    def get_evil_scientist(self, screen):
        screen.blit(self.enemy_image, self.enemy_rect)