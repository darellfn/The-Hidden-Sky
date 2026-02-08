import pygame
from components.background import Background
from components.ground import Ground
from characters.player import Player
from components.platform import Platform
from characters.evil_scientist import Evil_Scientist
from characters.enemy import Enemy
from components.item import Item
from components.pot import Pot
from components.beanstalk import Beanstalk
from components.wall import Wall

class Level_2:
    def __init__(self, screen):
        super().__init__

        self.completed = False

        # Background and ground
        self.screen = screen
        self.background = Background()
        self.ground = Ground()
        self.ground_pos_y = self.ground.get_ground_pos()

        # Platforms
        self.platform_1 = Platform(250, 550)
        self.platform_1_y = self.platform_1.get_platform()

        self.platform_2 = Platform(750, 550)
        self.platform_2_y = self.platform_2.get_platform()

        self.platform_3 = Platform(450, 315)
        self.platform_3_y = self.platform_3.get_platform()

        self.platform_4 = Platform(750, 315)
        self.platform_4_y = self.platform_4.get_platform()

        # Wall
        self.wall_1 = Wall(950, self.platform_4.get_top_point())
        self.wall_2 = Wall(950, self.wall_1.get_top_point())
        self.wall_3 = Wall(950, self.wall_2.get_top_point())

        # Player
        self.player = Player(self.ground_pos_y)

        # Enemy
        self.enemy = Enemy(650, self.platform_4.get_top_point())

        # Pot
        self.pot = Pot(1220, self.ground_pos_y, 80, 80, "graphics/items/pot.png")

        # Beanstalk
        self.beanstalk = Beanstalk(1220, self.ground_pos_y, 850, 600, "graphics/items/beanstalk.png")

        # Potion
        self.potion = Item(850, self.platform_4.get_top_point(), 40, 40, "graphics/items/potion.png")

        # Exit
        self.exit = Item(1300, 200, 50, 50, "graphics/items/exit.png")

    def start(self):
        keys = pygame.key.get_pressed()
        self.player.movement(keys)
        self.player.jump(keys)
        self.background.get_background(self.screen)
        self.ground.get_ground(self.screen)
        self.platform_1.draw_platform(self.screen)
        self.platform_2.draw_platform(self.screen)
        self.platform_3.draw_platform(self.screen)
        self.platform_4.draw_platform(self.screen)
        self.wall_1.draw_wall(self.screen)
        self.wall_2.draw_wall(self.screen)
        self.wall_3.draw_wall(self.screen)

        self.pot.draw_item(self.screen)
        self.potion.draw_item(self.screen)
        self.beanstalk_grow()
        self.potion.draw_item(self.screen)
        self.exit.draw_item(self.screen)
        self.enemy.spawn(self.screen)
        self.player.get_player(self.screen)
        self.player.change_y(self.platform_1_y)
        self.player.change_y(self.platform_2_y)
        self.player.change_y(self.platform_3_y)
        self.player.change_y(self.platform_4_y)
        self.player.add_item_to_inventory(keys, self.potion.get_rect(), self.potion)
        self.player.drop_item(self.potion, keys, self.beanstalk.get_beanstalk_rect())
        self.player.climb_beanstalk(keys, self.beanstalk, self.beanstalk.get_beanstalk_rect())
        self.finish_level()

    def beanstalk_grow(self):
        if self.pot.get_rect().colliderect(self.potion.get_rect()) and not self.potion.is_stored():
            self.beanstalk.draw_beanstalk(self.screen)
            self.beanstalk.grow_beanstalk()
        else:
            self.beanstalk.ungrow_beanstalk()

    def finish_level(self):
        if self.player.get_player_rect().colliderect(self.exit.get_rect()):
            self.is_finished()
    
    def is_finished(self):
        return self.completed
    
