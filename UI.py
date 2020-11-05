import pygame


class Screen:

    def __init__(self):
        self.screen_size = (1280, 720)
        self.color_white = (255, 255, 255)
        self.color_black = (0, 0, 0)
        self.speed = (2, 0)

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_size)
        self.font = pygame.font.Font(None, 32)

    def setup(self):
        pygame.display.set_caption("SpeedTypo")