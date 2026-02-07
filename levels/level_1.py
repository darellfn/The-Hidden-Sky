import pygame
from components.background import Background
from components.ground import Ground
from characters.player import Player
from components.platform import Platform
from characters.evil_scientist import Evil_Scientist
from components.item import Item

class Level_1:
    def __init__(self, screen):
        super().__init__

        # Background and ground
        self.screen = screen
        self.background = Background()
        self.ground = Ground()
        self.ground_pos_y = self.ground.get_ground_pos()

        # Platforms
        self.platform_1 = Platform(250, 550)
        self.platform_1_y = self.platform_1.get_platform()

        self.platform_2 = Platform(1200, 250)
        self.platform_2_y = self.platform_2.get_platform()

        # Player
        self.player = Player(self.ground_pos_y)

        # Evil Scientist
        self.evil_scientist = Evil_Scientist(self.ground_pos_y)

        # Pot

        self.pot = Item(800, self.ground_pos_y, 80, 80, "graphics/items/pot.png")

        # Beanstalk

        #self.beanstalk = Item(800, self.ground_pos_y, 850, 600, "graphics/items/beanstalk.png")

    def start(self):
        keys = pygame.key.get_pressed()
        self.player.movement(keys)
        self.player.jump(keys)
        self.background.get_background(self.screen)
        self.ground.get_ground(self.screen)
        self.platform_1.draw_platform(self.screen)
        self.platform_2.draw_platform(self.screen)
        self.pot.draw_item(self.screen)
        #self.beanstalk.draw_item(self.screen)
        self.player.get_player(self.screen)
        self.player.change_y(self.platform_1_y)
        self.player.change_y(self.platform_2_y)

    


