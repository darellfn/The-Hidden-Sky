import pygame 
from components.item import Item

class Player(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        self.player_size = (80, 80)
        self.y = y

        self.player_image = pygame.image.load("graphics/characters/rio/rio.png").convert_alpha()
        self.player_image = pygame.transform.flip(self.player_image, True, False)
        self.player_image = pygame.transform.scale(self.player_image, self.player_size)
        self.player_rect = self.player_image.get_rect(midbottom = (100, self.y))
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

        # Klatring
        self.player_climbing_index = 0
        self.player_climbing_1 = pygame.image.load("graphics/characters/rio/Rio_climbing.png").convert_alpha()
        self.player_climbing_2 = pygame.image.load("graphics/characters/rio/Rio_climbing_2.png").convert_alpha()
        self.player_climbing_3 = pygame.image.load("graphics/characters/rio/Rio_climbing_3.png").convert_alpha()

        self.climbing = [
            self.player_climbing_1,
            self.player_climbing_2,
            self.player_climbing_3
        ]

        self.is_climbing = False

        # Inventory
        self.inventory = []

    def get_player(self, screen):
        screen.blit(self.player_image, self.player_rect)

    def get_pos_x(self):
        return self.player_rect.x
    
    def get_pos_y(self):
        return self.player_rect.bottom
    
    def get_player_rect(self):
        return self.player_rect
    
    def movement(self, keys):
        # Venstre
        if self.player_rect.x >= 0:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.player_rect.x -= 8

                self.player_walking_left_index += 0.1
                if self.player_walking_left_index >= len(self.walking_left): 
                    self.player_walking_left_index = 0
                self.player_image = self.walking_left[int(self.player_walking_left_index)]
                self.player_image = pygame.transform.scale(self.player_image, self.player_size)

        # Høyre
        if self.player_rect.x <= 1325:
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.player_rect.x += 8

                self.player_walking_right_index += 0.1
                if self.player_walking_right_index >= len(self.walking_right): 
                    self.player_walking_right_index = 0
                self.player_image = self.walking_right[int(self.player_walking_right_index)]
                self.player_image = pygame.transform.scale(self.player_image, self.player_size)

        else:
            if not self.is_climbing:
                self.player_image = pygame.image.load("graphics/characters/rio/rio.png").convert_alpha()
                self.player_image = pygame.transform.scale(self.player_image, self.player_size)

    def jump(self, keys):
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity = self.jump_strength
            self.on_ground = False
        
        self.velocity += self.gravity
        self.player_rect.y += self.velocity

        if self.player_rect.bottom >= self.y:
            self.player_rect.bottom = self.y
            self.velocity = 0
            self.on_ground = True

    def change_y(self, platform_rect):
        if self.velocity >= 0:
            if self.player_rect.colliderect(platform_rect):
                if self.player_rect.bottom <= platform_rect.bottom:
                    self.player_rect.bottom = platform_rect.top
                    self.velocity = 0
                    self.on_ground = True

    def climb_beanstalk(self, keys, beanstalk, beanstalk_rect):
        if self.player_rect.colliderect(beanstalk_rect) and beanstalk.get_is_grown():
            if keys[pygame.K_UP]:
                self.is_climbing = True
                self.player_climbing_index += 0.1
                if self.player_climbing_index >= len(self.climbing):
                    self.player_climbing_index = 0
                
                self.player_image = self.climbing[int(self.player_climbing_index)]
                self.player_image = pygame.transform.scale(self.player_image, self.player_size)
                
                self.player_rect.y -= 5
                self.velocity = 0
                self.on_ground = False
            else:
                self.is_climbing = False

    def add_item_to_inventory(self, keys, item_rect, item):
        if self.player_rect.colliderect(item_rect):
            if keys[pygame.K_e]:
                if len(self.inventory) < 2:
                    self.inventory.append(item)
                    item.stored_in_inventory()

    def drop_item(self, item, keys, beanstalk):
        if self.player_rect.colliderect(beanstalk):
            if self.inventory:
                if keys[pygame.K_r]:
                    item.unstore_from_inventory(self.get_pos_x(), self.get_pos_y())
                    self.inventory.pop()




        


