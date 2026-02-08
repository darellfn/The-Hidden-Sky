import pygame

class Item:
    def __init__(self, x, y, height, width, path):
        super().__init__()
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.stored = False
        self.path = path
        
        self.item_image = pygame.image.load(self.path).convert_alpha()
        self.item_image = pygame.transform.scale(self.item_image, (self.width, self.height))
        self.item_pos = (self.x, self.y)
        self.item_rect = self.item_image.get_rect(midbottom = self.item_pos)

    def draw_item(self, screen):
        if not self.stored:
            screen.blit(self.item_image, self.item_rect)

    def get_rect(self):
        return self.item_rect
    
    def stored_in_inventory(self):
        self.stored = True

    def unstore_from_inventory(self, x, y):
        self.stored = False
        self.item_image = pygame.image.load(self.path).convert_alpha()
        self.item_image = pygame.transform.scale(self.item_image, (self.width, self.height))
        self.item_rect = self.item_image.get_rect(midbottom = (x, y))

    def is_stored(self):
        return self.stored



