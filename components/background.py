import pygame

class Background():
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load("test_graphics/sky.png").convert_alpha()
        self.background_pos = (0, 0)

    def get_background(self, screen):
        screen.blit(self.background, self.background_pos)
