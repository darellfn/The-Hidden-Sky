import pygame 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_size = (100, 100)

        self.player_image = pygame.image.load("graphics/characters/rio/rio.png").convert_alpha()
        self.player_image = pygame.transform.flip(self.player_image, True, False)
        self.player_image = pygame.transform.scale(self.player_image, self.player_size)
        self.player_rect = self.player_image.get_rect(midbottom = (100, 680))
        self.right = True
        self.left = False

        # Gravitet
        self.gravity = 0.7
        self.velocity = 0
        self.jump_strength = -20
        self.on_ground = True

        # Gå til venstre
        self.player_walking_left_index = 0
        self.player_walking_left_1 = pygame.image.load("graphics/characters/rio/Walking_Rio_left.png").convert_alpha()
        self.player_walking_left_2 = pygame.image.load("graphics/characters/rio/Walking_Rio_left_2.png").convert_alpha()
        self.player_walking_left_3 = pygame.image.load("graphics/characters/rio/Walking_Rio_left_3.png").convert_alpha()

        self.walking_left = [
            self.player_walking_left_1, 
            self.player_walking_left_2, 
            self.player_walking_left_3
        ]

        # Gå til høyre
        self.player_walking_right_index = 0
        self.player_walking_right_1 = pygame.image.load("graphics/characters/rio/Walking_Rio_right.png").convert_alpha()
        self.player_walking_right_2 = pygame.image.load("graphics/characters/rio/Walking_Rio_right_2.png").convert_alpha()
        self.player_walking_right_3 = pygame.image.load("graphics/characters/rio/Walking_Rio_right_3.png").convert_alpha()

        self.walking_right = [
            self.player_walking_right_1, 
            self.player_walking_right_2, 
            self.player_walking_right_3
        ]

    def get_player(self, screen):
        screen.blit(self.player_image, self.player_rect)

    def movement(self, keys):
        # Venstre
        if keys[pygame.K_LEFT]:
            self.player_rect.x -= 2
            if self.player_walking_left_index >= len(self.walking_left) - 1: 
                self.player_walking_left_index = 0

            self.player_walking_left_index += 0.1
            self.player_image = self.walking_left[int(self.player_walking_left_index)]
            self.player_image = pygame.transform.scale(self.player_image, self.player_size)

        # Høyre
        elif keys[pygame.K_RIGHT]:
            self.player_rect.x += 2
            if self.player_walking_right_index >= len(self.walking_right) - 1: 
                self.player_walking_right_index = 0

            self.player_walking_right_index += 0.1
            self.player_image = self.walking_right[int(self.player_walking_right_index)]
            self.player_image = pygame.transform.scale(self.player_image, self.player_size)

        else:
            self.player_image = pygame.image.load("graphics/characters/rio/rio.png").convert_alpha()
            self.player_image = pygame.transform.scale(self.player_image, self.player_size)

    def jump(self, keys):
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity = self.jump_strength
            self.on_ground = False
        
        self.velocity += self.gravity
        self.player_rect.y += self.velocity

        if self.player_rect.bottom >= 680:
            self.player_rect.bottom = 680
            self.velocity = 0
            self.on_ground = True

    def get_taller(self, keys):
        if keys[pygame.K_w]:
            width = self.player_rect.width
            new_height = self.player_rect.height + 1
        
            self.player_image = pygame.transform.scale(self.player_image, (width, new_height))

            self.player_rect = self.player_image.get_rect(midbottom = (self.player_rect.midbottom))

    def get_lower(self, keys):
        if keys[pygame.K_s]:
            width = self.player_rect.width
            new_height = self.player_rect.height - 1
        
            self.player_image = pygame.transform.scale(self.player_image, (width, new_height))

            self.player_rect = self.player_image.get_rect(midtop = (self.player_rect.midtop))

        


