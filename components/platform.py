import pygame

class Platform:
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y
        
        self.platform_surf_1 = pygame.image.load("graphics/platforms/platform_1.png").convert_alpha()
        self.platform_surf_1 = pygame.transform.scale(self.platform_surf_1, (500, 50))
        self.platform_1_rect = self.platform_surf_1.get_rect(midbottom = (self.x, self.y))

    def draw_platform(self, screen):
        screen.blit(self.platform_surf_1, self.platform_1_rect)

    def get_platform(self):
        return self.platform_1_rect