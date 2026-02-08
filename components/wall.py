import pygame

class Wall:
    def __init__(self, x, y):
        super().__init__
        self.x = x
        self.y = y
        
        self.wall_surf = pygame.image.load("graphics/wall/wall.png").convert_alpha()
        self.wall_surf = pygame.transform.scale(self.wall_surf, (100, 100))
        self.wall_rect = self.wall_surf.get_rect(midbottom = (self.x, self.y))

    def draw_wall(self, screen):
        screen.blit(self.wall_surf, self.wall_rect)

    def get_wall(self):
        return self.wall_rect
    
    def get_top_point(self):
        return self.wall_rect.top
    
    def get_left_point(self):
        return self.wall_rect.left