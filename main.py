import pygame
from sys import exit
from random import randint
from components.background import Background
from components.ground import Ground
from characters.player import Player
from components.platform import Platform
from levels.level_1 import Level_1
from levels.level_2 import Level_2
from levels.level_3 import Level_3
from screens.home import Home
from screens.lose import Lose
from levels.to_be_continued import To_Be_Continued

pygame.init()
screen = pygame.display.set_mode((1400, 850))
pygame.display.set_caption("The Hidden Sky")
clock = pygame.time.Clock()
game_over = False

# Lyd
main_theme = pygame.mixer.Sound("sounds/main_theme.mp3")
losing_sound = pygame.mixer.Sound("sounds/game_over.mp3")
victory_sound = pygame.mixer.Sound("sounds/cleared_level.mp3")

# Sound flags
main_theme_playing = False
sound_played = False

# Screens
home_screen = Home(screen)
losing_screen = Lose(screen)

# Levels
level_1 = Level_1(screen)
level_2 = Level_2(screen)
level_3 = Level_3(screen)

level_1_unlocked = True
level_2_unlocked = False
level_3_unlocked = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()

    if not home_screen.started():
        home_screen.draw()
        home_screen.start_game(keys)
    else:
        if not main_theme_playing and not game_over:
            main_theme.play(-1)
            main_theme_playing = True

        if not game_over:
            if level_1_unlocked:
                level_1.start()
                if level_1.is_finished():
                    level_2_unlocked = True

            if level_2_unlocked:
                if not level_2.is_detected():
                    level_2.start()
                    if level_2.is_finished():
                        level_3_unlocked = True
                else:
                    game_over = True

            if level_3_unlocked:
                if not level_3.is_detected():
                    level_3.start()
                    if level_3.is_finished():
                        if main_theme_playing:
                            main_theme.stop()
                            main_theme_playing = False

                        to_be_continued_screen = To_Be_Continued(screen)
                        to_be_continued_screen.show(victory_sound=victory_sound)

                        pygame.quit()
                        exit()
                else:
                    game_over = True
        else:
            if main_theme_playing:
                main_theme.stop()
                main_theme_playing = False

            losing_screen.draw()

            if not sound_played:
                losing_sound.play()
                sound_played = True

    pygame.display.update()
    clock.tick(60)