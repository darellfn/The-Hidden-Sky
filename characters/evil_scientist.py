import pygame

class Evil_Scientist:
    def __init__(self, y):
        super().__init__
        self.evil_scientist_size = (100, 100)
        self.y = y

        self.scientist_image = pygame.image.load("graphics/characters/evil_scientist/evil_scientist.png").convert_alpha()
        self.scientist_image = pygame.transform.scale(self.scientist_image, (self.evil_scientist_size))
        self.scientist_rect = self.scientist_image.get_rect(midbottom = (100, self.y))

    def get_evil_scientist(self, screen):
        screen.blit(self.scientist_image, self.scientist_rect)