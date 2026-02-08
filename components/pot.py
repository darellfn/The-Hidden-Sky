import pygame

class Pot:
    def __init__(self, x, y, height, width, path):
        super().__init__()
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        
        self.pot_image = pygame.image.load(path).convert_alpha()
        self.pot_image = pygame.transform.scale(self.pot_image, (width, height))
        self.pot_pos = (self.x, self.y)
        self.pot_rect = self.pot_image.get_rect(midbottom = self.pot_pos)

    def draw_item(self, screen):
        screen.blit(self.pot_image, self.pot_rect)

    def get_rect(self):
        return self.pot_rect