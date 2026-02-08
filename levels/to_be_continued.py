import pygame

class To_Be_Continued:
    def __init__(self, screen, font_size=100, color=(255, 255, 255)):
        self.screen = screen
        self.color = color
        self.font = pygame.font.Font("font/PixelifySans-Medium.ttf", font_size)
        self.text = self.font.render("TO BE CONTINUED...", True, self.color)
        self.rect = self.text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    def show(self, victory_sound=None):
        if victory_sound:
            victory_sound.play()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    running = False

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.text, self.rect)
            pygame.display.update()
            pygame.time.delay(10)