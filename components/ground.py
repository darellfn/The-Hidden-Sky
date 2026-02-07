import pygame

class Ground():
    def __init__(self):
        super().__init__()
        self.ground = pygame.image.load("test_graphics/ground.png")
        width, height = self.ground.get_size()
        self.ground = pygame.transform.scale(self.ground, (1400, height))
        self.ground_pos = (0, 650)

    def get_ground(self, screen):
        screen.blit(self.ground, self.ground_pos)