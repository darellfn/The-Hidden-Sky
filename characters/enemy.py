import pygame

class Enemy:
    def __init__(self, x, y):
        super().__init__()
        self.enemy_size = (100, 110)
        self.x = x
        self.y = y

        self.enemy_image = pygame.image.load("graphics/characters/enemies/swat.png").convert_alpha()
        self.enemy_image = pygame.transform.scale(self.enemy_image, self.enemy_size)
        self.enemy_rect = self.enemy_image.get_rect(midbottom=(self.x, self.y))

        self.enemy_walking_left_index = 0
        self.enemy_walking_left_1 = pygame.transform.scale(
            pygame.image.load("graphics/characters/enemies/swat_left.png").convert_alpha(),
            self.enemy_size
        )
        self.enemy_walking_left_2 = pygame.transform.scale(
            pygame.image.load("graphics/characters/enemies/swat_1_left.png").convert_alpha(),
            self.enemy_size
        )
        self.enemy_walking_left_3 = pygame.transform.scale(
            pygame.image.load("graphics/characters/enemies/swat_2_left.png").convert_alpha(),
            self.enemy_size
        )
        self.walking_left = [
            self.enemy_walking_left_1,
            self.enemy_walking_left_2,
            self.enemy_walking_left_3
        ]

        self.enemy_walking_right_index = 0
        self.enemy_walking_right_1 = pygame.transform.scale(
            pygame.image.load("graphics/characters/enemies/swat_right.png").convert_alpha(),
            self.enemy_size
        )
        self.enemy_walking_right_2 = pygame.transform.scale(
            pygame.image.load("graphics/characters/enemies/swat_1_right.png").convert_alpha(),
            self.enemy_size
        )
        self.enemy_walking_right_3 = pygame.transform.scale(
            pygame.image.load("graphics/characters/enemies/swat_2_right.png").convert_alpha(),
            self.enemy_size
        )
        self.walking_right = [
            self.enemy_walking_right_1,
            self.enemy_walking_right_2,
            self.enemy_walking_right_3
        ]

        self.moving_left = True

        self.vision_range = 250
        self.game_over_triggered = False

    def spawn(self, screen):
        screen.blit(self.enemy_image, self.enemy_rect)

    def walk(self, left_x, right_x):
        if self.moving_left:
            self.enemy_rect.x -= 1
            if self.enemy_rect.left <= left_x:
                self.moving_left = False

            self.enemy_walking_left_index += 0.1
            if self.enemy_walking_left_index >= len(self.walking_left):
                self.enemy_walking_left_index = 0

            self.enemy_image = self.walking_left[int(self.enemy_walking_left_index)]

        else:
            self.enemy_rect.x += 1
            if self.enemy_rect.right >= right_x:
                self.moving_left = True

            self.enemy_walking_right_index += 0.1
            if self.enemy_walking_right_index >= len(self.walking_right):
                self.enemy_walking_right_index = 0

            self.enemy_image = self.walking_right[int(self.enemy_walking_right_index)]

    def can_see_player(self, player_rect, walls=None):

        if self.moving_left:
            vision_rect = pygame.Rect(
                self.enemy_rect.left - self.vision_range,
                self.enemy_rect.top,
                self.vision_range,
                self.enemy_rect.height
            )
        else:
            vision_rect = pygame.Rect(
                self.enemy_rect.right,
                self.enemy_rect.top,
                self.vision_range,
                self.enemy_rect.height
            )

        if vision_rect.colliderect(player_rect):
            if walls:
                for wall in walls:
                    if wall.colliderect(vision_rect):
                        return False
            return True

        return False