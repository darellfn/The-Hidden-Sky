import pygame

class Beanstalk:
    def __init__(self, x, y, height, width, path):
        super().__init__()
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        
        self.beanstalk_image = pygame.image.load(path).convert_alpha()
        self.beanstalk_image = pygame.transform.scale(self.beanstalk_image, (width, height))
        self.beanstalk_pos = (self.x, self.y)
        self.beanstalk_rect = self.beanstalk_image.get_rect(midbottom = self.beanstalk_pos)

        self.grown = False

    def draw_beanstalk(self, screen):
        screen.blit(self.beanstalk_image, self.beanstalk_rect)

    def get_beanstalk_rect(self):
        return self.beanstalk_rect
    
    def grow_beanstalk(self):
        self.grown = True

    def ungrow_beanstalk(self):
        self.grown = False
    
    def get_is_grown(self):
        return self.grown