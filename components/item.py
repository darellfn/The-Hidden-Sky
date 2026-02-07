import pygame

class Item:
    def __init__(self, x, y, height, width, path):
        super().__init__()
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        
        self.item_image = pygame.image.load(path).convert_alpha()
        self.item_image = pygame.transform.scale(self.item_image, (width, height))
        self.item_pos = (self.x, self.y)
        self.item_rect = self.item_image.get_rect(midbottom = self.item_pos)

    def draw_item(self, screen):
        screen.blit(self.item_image, self.item_rect)