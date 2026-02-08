import pygame

class Lose:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.Font('font/PixelifySans-Medium.ttf', 80)
        self.text_font = pygame.font.Font('font/PixelifySans-Medium.ttf', 40)
        self.restart = False
        self.bg_color = (0, 0, 0)

    def draw(self):
        self.screen.fill(self.bg_color)

        title_text = self.title_font.render("You Got Spotted!", True, (255, 0, 0))
        title_rect = title_text.get_rect(center=(700, 300))
        self.screen.blit(title_text, title_rect)

        restart_text = self.text_font.render("Better luck next time", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(700, 500))
        self.screen.blit(restart_text, restart_rect)

    def handle_input(self, keys):
        if keys[pygame.K_SPACE]:
            self.restart = True

    def can_restart(self):
        return self.restart
