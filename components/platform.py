import pygame

class Platform:
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y
        
        self.platform_surf = pygame.image.load("graphics/platforms/platform_1.png").convert_alpha()
        self.platform_surf = pygame.transform.scale(self.platform_surf, (500, 50))
        self.platform_rect = self.platform_surf.get_rect(midbottom = (self.x, self.y))

    def draw_platform(self, screen):
        screen.blit(self.platform_surf, self.platform_rect)

    def get_platform(self):
        return self.platform_rect
    
    def get_top_point(self):
        return self.platform_rect.top
    
    def get_x_point(self):
        return self.platform_rect.x
    
    def get_right_point(self):
        return self.platform_rect.right
    
    def get_left_point(self):
        return self.platform_rect.left