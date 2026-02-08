import pygame
from components.background import Background
from components.ground import Ground
from characters.player import Player
from characters.enemy import Enemy
from components.platform import Platform
from characters.evil_scientist import Evil_Scientist
from components.item import Item
from components.pot import Pot
from components.beanstalk import Beanstalk

class Level_3:
    def __init__(self, screen):
        super().__init__

        self.completed = False

        # Background and ground
        self.screen = screen
        self.background = Background()
        self.ground = Ground()
        self.ground_pos_y = self.ground.get_ground_pos()

        # Platforms
        self.platform_1 = Platform(250, 600)
        self.platform_1_y = self.platform_1.get_platform()

        self.platform_2 = Platform(1200, 600)
        self.platform_2_y = self.platform_2.get_platform()

        self.platform_3 = Platform(250, 400)
        self.platform_3_y = self.platform_3.get_platform()

        self.platform_4 = Platform(1300, 250)
        self.platform_4_y = self.platform_4.get_platform()

        # Player
        self.player = Player(self.ground_pos_y)

        # Enemy
        self.enemy_1 = Enemy(self.platform_1.get_left_point(), self.platform_1.get_top_point())
        self.enemy_2 = Enemy(self.platform_2.get_right_point(), self.platform_2.get_top_point())
        self.enemy_3 = Enemy(self.platform_3.get_left_point(), self.platform_3.get_top_point())

        self.enemies = [
            self.enemy_1,
            self.enemy_2,
            self.enemy_3
        ]

        # Pot
        self.pot = Pot(750, self.ground_pos_y, 80, 80, "graphics/items/pot.png")

        # Beanstalk
        self.beanstalk = Beanstalk(780, self.ground_pos_y, 850, 600, "graphics/items/beanstalk.png")

        # Potion
        self.potion = Item(400, self.platform_3.get_top_point(), 40, 40, "graphics/items/potion.png")

        # Exit
        self.exit = Item(1250, 150, 100, 100, "graphics/items/exit.png")

    def start(self):
        keys = pygame.key.get_pressed()
        self.player.movement(keys, [])
        self.player.jump(keys)
        self.background.get_background(self.screen)
        self.ground.get_ground(self.screen)
        
        self.platform_1.draw_platform(self.screen)
        self.platform_2.draw_platform(self.screen)
        self.platform_3.draw_platform(self.screen)
        self.platform_4.draw_platform(self.screen)
        
        self.pot.draw_item(self.screen)
        self.potion.draw_item(self.screen)
        self.beanstalk_grow()
        self.potion.draw_item(self.screen)
        self.exit.draw_item(self.screen)

        self.enemy_1.spawn(self.screen)
        self.enemy_1.walk(self.platform_1.get_left_point(), self.platform_1.get_right_point())

        self.enemy_2.spawn(self.screen)
        self.enemy_2.walk(self.platform_2.get_left_point(), self.platform_2.get_right_point())

        self.enemy_3.spawn(self.screen)
        self.enemy_3.walk(self.platform_3.get_left_point(), self.platform_3.get_right_point())


        self.player.get_player(self.screen)
        self.player.change_y(self.platform_1_y)
        self.player.change_y(self.platform_2_y)
        self.player.change_y(self.platform_3_y)
        self.player.change_y(self.platform_4_y)
        self.player.add_item_to_inventory(keys, self.potion.get_rect(), self.potion)
        self.player.drop_item(self.potion, keys, self.beanstalk.get_beanstalk_rect())
        self.player.climb_beanstalk(keys, self.beanstalk, self.beanstalk.get_beanstalk_rect())
        self.finish_level()

    def is_detected(self):
        for enemy in self.enemies:
            if enemy.can_see_player(self.player.get_player_rect()):
                return True

    def beanstalk_grow(self):
        if self.pot.get_rect().colliderect(self.potion.get_rect()) and not self.potion.is_stored():
            self.beanstalk.draw_beanstalk(self.screen)
            self.beanstalk.grow_beanstalk()
        else:
            self.beanstalk.ungrow_beanstalk()

    def finish_level(self):
        if self.player.get_player_rect().colliderect(self.exit.get_rect()):
            self.completed = True
    
    def is_finished(self):
        return self.completed