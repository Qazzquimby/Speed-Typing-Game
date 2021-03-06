import pygame


class Screen:

    def __init__(self, size, name):
        self.size = size
        pygame.display.set_caption(name)

        self.color_white = (255, 255, 255)
        self.color_black = (0, 0, 0)

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(tuple(self.size))
        self.font = pygame.font.Font(None, 32)
