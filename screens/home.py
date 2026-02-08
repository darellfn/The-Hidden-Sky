import pygame

class Home:
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.font = pygame.font.Font('font/PixelifySans-Medium.ttf', 100)
        self.start_font = pygame.font.Font('font/PixelifySans-Medium.ttf', 30)
        self.at_start = False
        self.tutorial_font = pygame.font.Font('font/PixelifySans-Medium.ttf', 30)

    def draw(self):
        self.background()
        self.title()
        self.start()

    def background(self):
        background = pygame.image.load("graphics/backgrounds/home_background.png").convert_alpha()
        self.screen.blit(background, (0, 0))

    def title(self):
        title = self.font.render("The Hidden Sky", False, "White")
        title_rect = title.get_rect(center = (700, 200))
        self.screen.blit(title, title_rect)

    def start(self):
        lines = [
            "A or < : Move Left",
            "D or > : Move Right",
            "W or ^"
            "SPACE : Jump",
            "E : Pick up potion",
            "R : Drop potion on flower pot",
            "",
            "Main objective:",
            "Escape the underground lab without getting spotted,",
            "use potion and drop it on the pots to grow beanstalks...",
            "",
            "Double-press 'SPACE' to start the game"
        ]

        y = 300
        for line in lines:
            text = self.tutorial_font.render(line, False, "White")
            self.screen.blit(text, text.get_rect(center=(700, y)))
            y += 40

    def started(self):
        return self.at_start

    def start_game(self, keys):
        if keys[pygame.K_SPACE]:
            self.at_start = True

    def can_start(self):
        return self.at_start