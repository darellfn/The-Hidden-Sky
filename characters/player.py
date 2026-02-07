import pygame 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_image = pygame.image.load("test_graphics/characters/test_cat.png")
        self.player_image = pygame.transform.flip(self.player_image, True, False)
        self.player_image = pygame.transform.scale(self.player_image, (100, 100))
        self.player_rect = self.player_image.get_rect(midbottom = (100, 680))

    def get_player(self, screen):
        screen.blit(self.player_image, self.player_rect)

    def movement(self, keys):
        if keys[pygame.K_LEFT]:
            self.player_rect.x -= 2
        elif keys[pygame.K_RIGHT]:
            self.player_rect.x += 2