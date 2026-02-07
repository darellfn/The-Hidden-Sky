import pygame

class Ground():
    def __init__(self):
        super().__init__()
        self.ground = pygame.image.load("graphics/platforms/platform_1.png")
        width, height = self.ground.get_size()
        self.ground = pygame.transform.scale(self.ground, (1400, height))
        self.ground_pos = (0, 750)

    def get_ground(self, screen):
        screen.blit(self.ground, self.ground_pos)

    def get_ground_pos(self):
        x, y = self.ground_pos
        return y